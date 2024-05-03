import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch HTML content")
        return None

def scrape_data(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        data = []
        table = soup.find('table', id='example2')
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            country_rank = columns[0].text.strip()
            country_name = columns[1].text.strip()
            gdp_nominal = columns[2].text.strip()
            gdp_growth = columns[3].text.strip()
            population_2022 = columns[4].text.strip()
            gdp_per_capita = columns[5].text.strip()
            share_of_world_gdp = columns[6].text.strip()
          
            data.append({
                '#': country_rank,
                'Country': country_name,
                'GDP (nominal, 2022)': gdp_nominal,
                'GDP growth': gdp_growth,
                'Population (2022)': population_2022,
                'GDP per capita': gdp_per_capita,
                'Share of World GDP': share_of_world_gdp
            })
        return data
    else:
        return None

def store_data_to_csv(data):
    if data:
        headers = ['#', 'Country', 'GDP (nominal, 2022)', 'GDP growth', 'Population (2022)', 'GDP per capita', 'Share of World GDP']
        with open('world_gdp_data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for item in data:
                writer.writerow(item)

def main():
    url = "https://www.worldometers.info/gdp/gdp-by-country/"
    html_content = fetch_html(url)
    if html_content:
        data = scrape_data(html_content)
        if data:
            store_data_to_csv(data)
            print("Data stored successfully in world_gdp_data.csv")
        else:
            print("Failed to scrape data from the HTML")
    else:
        print("Failed to fetch HTML content from the URL")

if __name__ == "__main__":
    main()
