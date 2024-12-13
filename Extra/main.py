import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file (adjust path as necessary)
data = pd.read_csv('HE Attrition Data Main, 2005-2013.csv')

attrition_columns = [
    'nesbattrition', 'disattrition', 'seslow2006attrition', 'seslow2011attrition', 'indigenousattrition',
    'modeinternalatt', 'modeexternalatt', 'modemultiatt', 'typeftatt', 'typeptatt', 'genderfemaleatt',
    'gendermaleatt', 'ageunder25att', 'age25to39att', 'agegt39att', 'boahigheredatt', 'boasecondaryatt',
    'boavetatt', 'boamatureatt', 'boaproffatt', 'boaotheratt', 'atarunder70att', 'atar70to89att', 'atargt89',
    'bfoescienceatt', 'bfoeITatt', 'bfoeengineeratt', 'bfoearchatt', 'bfoeagricatt', 'bfoehealthatt', 
    'bfoeeducatt', 'bfoemanageatt', 'bfoesocietyatt', 'bfoeartsatt'
]

years = ['2005','2006','2007','2008','2009','2010','2011','2012', '2013']  
trend_data = []
for column in attrition_columns:
    attrition_values = data[column].values
    # Using linear regression model to find clusters based on trend of attrition over time period
    model = LinearRegression()
    model.fit(np.array([2006, 2011]).reshape(-1, 1), attrition_values[:2]) 
    
    trend = model.coef_[0]
    
    trend_data.append(trend)

trend_df = pd.DataFrame({
    'Attribute': attrition_columns,
    'Trend': trend_data
})

def classify_risk(slope):
    if slope > 0:
        return 'High Risk'  # +ve slope: increasing attrition over period
    elif slope > -0.05:
        return 'Intermediate Risk'  # Slightly -ve slope: neutral to small decrease attrition over period
    else:
        return 'Low Risk'  # Strong -ve slope: decreasing attrition across over period

trend_df['Risk_Category'] = trend_df['Trend'].apply(classify_risk)

trend_df = trend_df.sort_values(by='Trend', ascending=False)

plt.figure(figsize=(10, 6))

colors = {'High Risk': 'red', 'Intermediate Risk': 'orange', 'Low Risk': 'green'}
color_list = trend_df['Risk_Category'].map(colors)

start = 0
for idx, row in trend_df.iterrows():
    plt.barh(row['Attribute'], row['Trend'], left=start, color=color_list[idx], edgecolor='black')
    start += row['Trend']

for idx, row in trend_df.iterrows():
    plt.text(
        start - row['Trend'] / 2,
        idx, 
        f"{row['Risk_Category']}", 
        color='white', 
        ha='center', 
        va='center'
    )


plt.xlabel('Trend (Slope) of Attrition Rate')
plt.title('Waterfall Chart of Attrition Trends by Risk Category')


handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors.values()]
labels = list(colors.keys())
plt.legend(handles, labels, title='Risk Category')

plt.tight_layout()
plt.show()

# Printing classification report
print(trend_df)
