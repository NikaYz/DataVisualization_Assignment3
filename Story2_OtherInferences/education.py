import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change file path accordingly
df = pd.read_csv("../Database/HE Attrition Data Main, 2005-2013.csv" )
df['science_IT'] = df['bfoescienceatt'] + df['bfoeITatt']
df['engineering_tech'] = df['bfoeengineeratt'] + df['bfoearchatt'] + df['bfoeagricatt']
df['health_education'] = df['bfoehealthatt'] + df['bfoeeducatt']
df['business_management'] = df['bfoemanageatt'] + df['bfoesocietyatt']
df['arts_education'] = df['bfoeartsatt']

# Creating a new DataFrame with just the year and the new features
new_columns = ['science_IT', 'engineering_tech', 'health_education', 
               'business_management', 'arts_education']
plot_data = df[['Reference_year'] + new_columns]

plt.figure(figsize=(10, 6))
for column in new_columns:
    plt.plot(plot_data['Reference_year'], plot_data[column], label=column)

plt.title('Attrition by Broader Education Fields (2005-2013)')
plt.xlabel('Year')
plt.ylabel('Attrition Rate')
plt.legend(title='Field Categories')

plt.grid(True)
plt.tight_layout()
plt.savefig('combined_field_education.png', dpi=50)
plt.show()