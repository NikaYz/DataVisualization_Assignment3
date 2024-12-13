import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Database/HE Attrition Data Main, 2005-2013.csv")

# Function to create interaction terms and plot
def plot_interaction(ses_column, year_range, save_path):
    education_columns = ['boahigheredatt', 'boasecondaryatt', 'boavetatt', 
                         'boamatureatt', 'boaproffatt', 'boaotheratt']
    
    # Create interaction terms
    for edu_col in education_columns:
        interaction_column = f'{ses_column}_x_{edu_col}'
        df[interaction_column] = df[ses_column] * df[edu_col]
    
    # Create a new DataFrame for plotting
    interaction_columns = [f'{ses_column}_x_{edu_col}' for edu_col in education_columns]
    interaction_data = df[['Reference_year'] + interaction_columns]

    # Plot each interaction term as a line for each year
    plt.figure(figsize=(10, 6))
    for column in interaction_columns:
        plt.plot(interaction_data['Reference_year'], interaction_data[column], label=column)
    
    # Add titles and labels
    plt.title(f'Interaction Between {ses_column} and Education Type ({year_range})')
    plt.xlabel('Year')
    plt.ylabel('Interaction Term (SES x Education Type)')
    plt.legend(title='Interaction Terms')
    plt.grid(True)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(save_path)
    plt.close()

# Plot and save for seslow2006attrition
plot_interaction('seslow2006attrition', '2005-2013', 'interaction_ses2006.png')

# Plot and save for seslow2011attrition
plot_interaction('seslow2011attrition', '2005-2013', 'interaction_ses2011.png')
