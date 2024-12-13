import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Change file path accordingly
data = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv')  
def create_radar_chart(data, year):
    categories = ['nesbattrition', 'disattrition', 'indigenousattrition', 'seslow2006attrition', 'seslow2011attrition','modeinternalatt','modeexternalatt','modemultiatt','typeftatt','typeptatt','genderfemaleatt','gendermaleatt','ageunder25att','age25to39att','agegt39att', 'bfoescienceatt', 'bfoeITatt', 'bfoeengineeratt', 'bfoearchatt',
    'bfoeagricatt', 'bfoehealthatt', 'bfoeeducatt', 'bfoemanageatt',
    'bfoesocietyatt', 'bfoeartsatt','boahigheredatt', 'boasecondaryatt', 'boavetatt', 'boamatureatt', 'boaproffatt', 'boaotheratt']

    # Filtering and process the data for the given year
    radar_data = data[data['Reference_year'] == year][categories].values.flatten()
    
    # Normalizing so that it's between 0 to 1
    radar_data = radar_data / np.max(radar_data)
    
    # Set up radar plot
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]
    
    # Radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
    ax.plot(angles, np.append(radar_data, radar_data[0]), color='red', linewidth=2, linestyle='solid')
    ax.fill(angles, np.append(radar_data, radar_data[0]), color='red', alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title(f'Attrition Rates by Demographic Categories ({year})')
    plt.savefig(f'Radar_chart_({year})', dpi=100)
    plt.show()
    

def create_radar_charts_for_years(data):
    # Looping through each unique year in the dataset and create a radar chart
    years = data['Reference_year'].unique()
    
    for year in years:
        create_radar_chart(data, year)
create_radar_charts_for_years(data)