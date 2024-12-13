import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import plotly.express as px
import matplotlib.colors as mcolors

# Change file path accordinlgy
data = pd.read_csv("../Database/HE Attrition Data Main, 2005-2013.csv" )

bfoe_columns = [
    'bfoescienceatt', 'bfoeITatt', 'bfoeengineeratt', 'bfoearchatt',
    'bfoeagricatt', 'bfoehealthatt', 'bfoeeducatt', 'bfoemanageatt',
    'bfoesocietyatt', 'bfoeartsatt'
]
trend_data = []

for col in bfoe_columns:
    # Using Linear Regression to calculate the slope (trend) of the attrition rate
    X = np.array(data['Reference_year']).reshape(-1, 1)
    y = data[col].values  # Attrition rates as the dependent variable
    model = LinearRegression()
    model.fit(X, y)
    
    # Store the slope (trend) value for each field of education
    trend_data.append(model.coef_[0])  # coef_ gives the slope

# Performing clustering based on trends
trend_data = np.array(trend_data).reshape(-1, 1)

# Normalizing
scaler = StandardScaler()
trend_data_scaled = scaler.fit_transform(trend_data)

# Applying K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(trend_data_scaled)

# Adding labels
clustered_fields = pd.DataFrame({'Field of Education': bfoe_columns, 'Trend Slope': trend_data.flatten(), 'Cluster': clusters})

# Visualizing plot
plt.figure(figsize=(10, 6))

# Creating color map for three clusters
cmap = mcolors.ListedColormap(['#FF6347', '#4682B4', '#32CD32']) 

scatter = plt.scatter(clustered_fields['Field of Education'], clustered_fields['Trend Slope'], 
                      c=clustered_fields['Cluster'], cmap=cmap)

# Adding title and labels
plt.title('Clustering of Fields of Education Based on Trend Slope')
plt.xlabel('Field of Education')
plt.ylabel('Trend Slope (Rate of Change in Attrition)')

# Rotate x-axis labels to make them fully visible
plt.xticks(rotation=45, ha="right")

# Add color bar for clusters with labels as 1, 2, 3
cbar = plt.colorbar(scatter)
cbar.set_ticks([0, 1, 2])
cbar.set_label('Cluster')
cbar.set_ticklabels([1, 2, 3])

# Show the plot
plt.tight_layout()

# Save the image
plt.savefig('clustered_fields_of_education.png', dpi=50)

# Show the plot
plt.show()