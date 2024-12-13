import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.patches as mpatches


data = pd.read_csv('../Database/HE Attrition Data Main, 2005-2013.csv')

# Groupings done on the basis for the data based on my analysis (can be changed to one's opinion)
groupings = {
    'General': [ 'nesbattrition', 'disattrition', 'seslow2006attrition', 'seslow2011attrition', 'indigenousattrition'],
    'Study Mode': ['modeinternalatt', 'modeexternalatt', 'modemultiatt'],
    'Study Type': ['typeftatt', 'typeptatt'],
    'Gender': ['genderfemaleatt', 'gendermaleatt'],
    'Age': ['ageunder25att', 'age25to39att', 'agegt39att'],
    'BOA': ['boahigheredatt', 'boasecondaryatt', 'boavetatt', 'boamatureatt', 'boaproffatt', 'boaotheratt'],
    'ATAR': ['atarunder70att', 'atar70to89att', 'atargt89'],
    'BFOE': ['bfoescienceatt', 'bfoeITatt', 'bfoeengineeratt', 'bfoearchatt', 'bfoeagricatt', 'bfoehealthatt', 
             'bfoeeducatt', 'bfoemanageatt', 'bfoesocietyatt', 'bfoeartsatt']
}

# Calculating the average value for each group
group_averages = {}
for group, columns in groupings.items():
    group_averages[group] = data[columns].mean().mean()

# Extracing labels and average values
labels = list(group_averages.keys())
values = list(group_averages.values())

# Verifying the min and max averages (was giving errors)
vmin, vmax = min(values), max(values)
print(f"Colormap Range - Min: {vmin}, Max: {vmax}")

# Normalizing the data for the colormap
norm = Normalize(vmin=vmin, vmax=vmax)
cmap = cm.get_cmap('viridis')  # Can change accordingly to ur opinion
colors = [cmap(norm(value)) for value in values]  # Applying normalization

# Plot the donut chart basically it's a pie chart with a white circle above
fig, ax = plt.subplots(figsize=(10, 10))

wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    colors=colors,
)

# Adding a white center circle for the donut effect
center_circle = plt.Circle((0, 0), 0.70, color='white')
ax.add_artist(center_circle)

# Styling the text and title
plt.setp(autotexts, size=8, weight="bold")
ax.set_title('Donut Chart of Average Attrition Data by Group', fontsize=16)


# Creating a legend to show the group labels and values
legend_patches = [mpatches.Patch(color=colors[i], label=f"{labels[i]}: {values[i]:.2f}") for i in range(len(labels))]
ax.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5), title="Groups")
plt.savefig('average_attrition_donut_chart.png', format='png', dpi=50, bbox_inches='tight')

plt.tight_layout()
plt.show()
