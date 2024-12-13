import plotly.express as px
import pandas as pd

# Change file path accordingly
df = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv')

# Diving it into categories
melted_df = df.melt(id_vars='Reference_year', var_name='category', value_name='value')

# Handle missing or zero values
melted_df['value'].fillna(0.01, inplace=True)  # Replace NaN with a small constant
melted_df = melted_df[melted_df['value'] > 0]  # Ensure no zero values remain

# Creating a sunburst chart with color scale
fig = px.sunburst(
    melted_df,
    path=['Reference_year', 'category'],
    values='value',
    title='Sunburst Chart of Attributes Year-wise',
    color='value',
    color_continuous_scale='Viridis'  # CHange color map accordingly
)

# Show the plot
fig.show()
