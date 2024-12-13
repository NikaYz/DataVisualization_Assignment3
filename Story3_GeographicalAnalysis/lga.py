import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

# Change path accordingly
data = pd.read_csv('../Database/LGA HE Attrition Data, 2005-2013.csv')

# Display the first few rows to understand the structure
print("Initial Data Preview:")
print(data.head())

#Converting the year columns (2005-2013) to numeric values
year_columns = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
data[year_columns] = data[year_columns].apply(pd.to_numeric, errors='coerce')

#Preprocess:  missing values using the mean strategy
imputer = SimpleImputer(strategy='mean')
data[year_columns] = imputer.fit_transform(data[year_columns])

features = data[year_columns]

# Normalizing the features for clustering
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # Adjust the number of clusters as needed
data['Cluster'] = kmeans.fit_predict(scaled_features)

# Saving the updated dataset with clusters to use in Tableau
output_file = 'LGA_HE_Attrition_with_Clusters.csv'
data.to_csv(output_file, index=False)
print(f"File saved with clusters added: {output_file}")

# Visualizing the clusters on a bar chart
plt.figure(figsize=(10, 8))
sns.countplot(x='Cluster', data=data, palette='viridis')
plt.title('Distribution of LGAs in Different Clusters')
plt.xlabel('Cluster')
plt.ylabel('Number of LGAs')
plt.show()

# Step 8: Analyze the clusters
cluster_summary = data.groupby('Cluster').agg({
    **{year: ['mean', 'std'] for year in year_columns}
})
print("Cluster Summary Statistics:")
print(cluster_summary)
