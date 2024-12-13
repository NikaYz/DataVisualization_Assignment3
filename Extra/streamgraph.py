import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import plotly.express as px

# Change file path accordingly
data = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv')  
data['Reference_year'] = data['Reference_year'].astype(str)

# Changing data format accordingly
stream_data_melted = data.melt(id_vars=['Reference_year'], 
                               var_name='category', 
                               value_name='value')

# Creating stream for each year, so we group by 'Reference_year' and 'category'
fig = px.area(stream_data_melted, 
              x="Reference_year", 
              y="value", 
              color="category", 
              line_group="category", 
              title="Streamgraph of Various Attrition and Other Rates by Year")

# Customizing appearance (optional)
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Rate",
    template="plotly_dark",
    showlegend=True
)

# Show the streamgraph
fig.show()