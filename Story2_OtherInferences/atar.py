import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Change path file accordingly
file_path = "../Database/HE Attrition Data Main, 2005-2013.csv" 
data = pd.read_csv(file_path)

# Computing the Weighted ATAR based on analysis
data['Weighted_ATAR'] = (0.3 * data['atarunder70att'] + 
                         0.5 * data['atar70to89att'] + 
                         0.2 * data['atargt89'])

# Observing first rows to get inference
print(data[['Reference_year', 'attrition_rate', 'Weighted_ATAR']].head(9))
print(data['Reference_year'].unique())
# Analyzing correlation between Weighted_ATAR and attrition_rate
correlation = data['Weighted_ATAR'].corr(data['attrition_rate'])
print(f"Correlation between Weighted ATAR and Attrition Rate: {correlation:.4f}")

# Yearly trend analysis
plt.figure(figsize=(12, 6))
sns.lineplot(x='Reference_year', y='Weighted_ATAR', data=data, label='Weighted ATAR', marker='o')
sns.lineplot(x='Reference_year', y='attrition_rate', data=data, label='Attrition Rate', marker='o')
plt.title('Yearly Trends: Weighted ATAR vs Attrition Rate', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig("Atar_score_mean",dpi=50)
plt.show()
