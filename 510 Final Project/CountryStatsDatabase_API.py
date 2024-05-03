import requests
import pandas as pd

url = "https://countrystats-database.p.rapidapi.com/country-health-indicators"
headers = {
    'X-RapidAPI-Key': 'd05d492492msh70463afbbefeb53p14a511jsn8fd422edcf26',
    "X-RapidAPI-Host": "countrystats-database.p.rapidapi.com"
}
def fetch_country_data(country):
    params = {"country": country}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {country} from the API")
        return None

def main():
    with open("countries.txt", "r") as file:
        countries = file.read().splitlines()

    data = []

    for country in countries:
        country_data = fetch_country_data(country)
        if country_data:
            data.append({
                "Country": country,
                "Immunization, DPT (% of children ages 12-23 months)": country_data.get('2021', {}).get('Immunization, DPT (% of children ages 12-23 months)', None),
                "Death rate, crude (per 1,000 people)": country_data.get('2021', {}).get('Death rate, crude (per 1,000 people)', None),
                "Birth rate, crude (per 1,000 people)": country_data.get('2021', {}).get('Birth rate, crude (per 1,000 people)', None),
                "Diabetes prevalence (% of population ages 20 to 79)": country_data.get('2021', {}).get('Diabetes prevalence (% of population ages 20 to 79)', None),
                "Life expectancy at birth, total (years)": country_data.get('2021', {}).get('Life expectancy at birth, total (years)', None),
                "Mortality rate, under-5 (per 1,000 live births)": country_data.get('2021', {}).get('Mortality rate, under-5 (per 1,000 live births)', None),
                "Adolescent fertility rate (births per 1,000 women ages 15-19)": country_data.get('2021', {}).get('Adolescent fertility rate (births per 1,000 women ages 15-19)', None),
                "Incidence of tuberculosis (per 100,000 people)": country_data.get('2021', {}).get('Incidence of tuberculosis (per 100,000 people)', None),
                "Population growth (annual %)": country_data.get('2021', {}).get('Population growth (annual %)', None),
                "Population, total": country_data.get('2021', {}).get('Population, total', None),
                "Prevalence of undernourishment (% of population)": country_data.get('2021', {}).get('Prevalence of undernourishment (% of population)', None),
            })

    df = pd.DataFrame(data)
    df.to_csv("country_stats.csv", index=False)

    if data:
        print("Data stored successfully in country_stats.csv")
    else:
        print("Failed to fetch and store data")

if __name__ == "__main__":
    main()
