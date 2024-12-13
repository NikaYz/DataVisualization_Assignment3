import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the dataset
data = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv')

# One can choose columns based on your interest, here I have selected all numerical columns
heatmap_data = data.iloc[:, 1:].set_index(data['Reference_year'])

# Plot heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data.T, cmap='coolwarm', annot=False, cbar=True)
plt.title('Attrition Rates Across Different Categories (2005-2013)')
plt.xlabel('Year')
plt.ylabel('Categories')
plt.show()
plt.savefig('Attrition Rates Across Different Categories.png', dpi=100)