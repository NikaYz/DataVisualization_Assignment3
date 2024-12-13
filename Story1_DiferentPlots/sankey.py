import pandas as pd
# Using go to plot Sankey
import plotly.graph_objects as go


df = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv') 
sources = []
targets = []
values = []

for _, row in df.iterrows():
    year = row['Reference_year']
    for column in df.columns[1:]:
        sources.append(year)
        targets.append(column)
        values.append(row[column])

# Converting sources and targets into unique indices
all_nodes = list(set(sources + targets))
node_indices = {node: idx for idx, node in enumerate(all_nodes)}

sources_idx = [node_indices[source] for source in sources]
targets_idx = [node_indices[target] for target in targets]

#Creating the Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes
    ),
    link=dict(
        source=sources_idx,
        target=targets_idx,
        value=values
    )
))

fig.update_layout(title_text="Sankey Diagram of Year-Wise Data", font_size=10)
fig.show()