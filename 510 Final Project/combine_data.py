import pandas as pd

# Read the CSV files
df_gdp = pd.read_csv("world_gdp_data.csv")
df_country_stats = pd.read_csv("country_stats.csv")
df_happiness = pd.read_csv('cleaned_happiness_dataset.csv')

# Merge the dataframes
combined_data = pd.merge(df_gdp, df_country_stats, on='Country')
combined_data = pd.merge(combined_data, df_happiness, how='left', left_on='Country', right_on='Country or region')

# Rename columns
combined_data.rename(columns={'Immunization, DPT (% of children ages 12-23 months)': 'Immunization (%)',
                              'Death rate, crude (per 1,000 people)': 'Death rate/1000 people',
                              'Birth rate, crude (per 1,000 people)': 'Birth rate/1000 people',
                              'Life expectancy at birth, total (years)': 'Life expectancy'}, inplace=True)

# Remove unwanted characters from string columns
combined_data = combined_data.apply(lambda x: x.str.replace(',', '').str.replace('%', '').str.replace('$', '') if x.dtype == 'object' else x)

# Drop the 'Country or region' column
combined_data.drop(columns=['Country or region'], inplace=True)
combined_data.to_csv('combined_data.csv', index=False)

print("Combined data saved successfully to combined_data.csv")

