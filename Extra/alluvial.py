import pandas as pd
import plotly.graph_objects as go

# change the csv file path
df = pd.read_csv('../HE Attrition Data Main, 2005-2013.csv') 

# Mapping the categories
years = df['Reference_year'].unique()
modes = ['modeinternalatt', 'modeexternalatt', 'modemultiatt']

# Preparing the nodes and links
nodes = list(years) + modes 

# Create the flow of data (links)
links = []

# For each year, we calculate the total attrition for each mode
for i, year in enumerate(years):
    year_data = df[df['Reference_year'] == year]
    
    # Internal mode attrition
    internal_attrition = year_data['modeinternalatt'].sum()
    # External mode attrition
    external_attrition = year_data['modeexternalatt'].sum()
    # Multi mode attrition
    multi_attrition = year_data['modemultiatt'].sum()
    
    # Append the links for this year -> mode attrition
    links.append([i, len(years) + 0, internal_attrition])  # Year -> Internal
    links.append([i, len(years) + 1, external_attrition])  # Year -> External
    links.append([i, len(years) + 2, multi_attrition])    # Year -> Multi

# Convert links to plotly format
link_sources = [link[0] for link in links]
link_targets = [link[1] for link in links]
link_values = [link[2] for link in links]

# Create the Alluvial Diagram using Plotly
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes
    ),
    link=dict(
        source=link_sources,
        target=link_targets,
        value=link_values
    )
))

# Update layout for better visual appearance
fig.update_layout(
    title_text="Alluvial Diagram of Attrition Rates Across Years and Modes",
    font_size=10,
)

fig.show()