import pandas as pd

# Read the CSV file
df = pd.read_csv('happiness dataset.csv')

# Define the columns to keep
columns_to_keep = ['Country or region', 'Overall rank', 'Score_2016', 'Score_2017', 'Score_2018', 'Score_2019', 'Score_2020', 'Score_2021', 'Score_2022']

# Select the desired columns
df_cleaned = df[columns_to_keep]

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_happiness_dataset.csv', index=False)

print("Data saved successfully to cleaned_happiness_dataset.csv")

