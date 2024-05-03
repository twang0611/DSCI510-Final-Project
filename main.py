import streamlit as st
import pandas as pd
import plotly.express as px

df_combined = pd.read_csv("combined_data.csv")

def instruction():
    st.title("Investigating the features of country data and the relationship between economic factors, health indicators, and the happiness index across countries.")

    st.header("**Tong Wang**")


    st.write("**2. An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc.**")
    st.write("The web application is designed to provide users with an interactive experience in exploring the features of world data and the relationship between economic factors, health indicators, and the happiness index across countries. Upon accessing the webapp, it provides a user-friendly interface featuring a table displaying various features for each country, including economic metrics, health statistics, and happiness index scores. This table serves as a comprehensive overview of the dataset, allowing users to scrutinize the specific attributes of individual countries. Additionally, the webapp includes a scatter plot that visually depicts the relationship between selected economic factors, health indicators, and happiness index scores. Through intuitive interactive features, users can effortlessly customize the variables displayed on the scatter plot, enabling dynamic exploration of the data. Through feature selection, users can pinpoint specific variables of interest from the dataset, such as GDP per capita, life expectancy, or happiness index scores, enabling focused analysis tailored to their research objectives. Additionally, the option for country filtering empowers users to narrow down their investigation to one or multiple countries, fostering comparative studies and regional insights. The inclusion of a slider bar for adjusting the GDP range further enhances flexibility in data exploration, allowing users to hone in on countries within specific economic brackets. It also has a dynamic updates feature that ensures that as users modify their selections, the table and scatter plot seamlessly reflect these changes in real time, providing immediate insights into how data patterns evolve across different parameters.")

    st.write("**3.	Any major “gotchas” (i.e. things that don’t work, go slowly, could be improved, etc.)**")
    st.write("One significant challenge lies in the data sources themselves, as they lack the comprehensive information necessary to facilitate a thorough analysis. Additionally, when dealing with API data sources, the authentication requirements and request limitations posed hurdles to data retrieval and processing. ")


def page_conclusion():
    st.title("Conclusion")

    st.write("**4.	What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)**.")
    st.write("The motivation for this project is to investigate the features of country data and explore the complex relationship between economic factors, health indicators, and the happiness index across diverse nations. By analyzing comprehensive datasets encompassing world GDP, country health indicators, and happiness index scores, the primary objective is to unravel the multifaceted dynamics underlying national well-being, it seeks to contribute valuable insights to the understanding of societal well-being and inform evidence-based policy decisions aimed at fostering happier and healthier communities globally.")

    st.write("Also, I've changed my topic and datasets. In Milestone 1, I attempted to scrape Twitter tweets, but I encountered huge difficulties. I found it's really hard to scrape tweets. Therefore, I've opted to switch my topic.")
    
    st.write("**5.	What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)**")
    st.write("Throughout the project, I discovered that the happiness score exhibits a robust positive correlation with life expectancy while displaying only a weak correlation with immunization rates and a negligible relationship with diabetes prevalence. The happiness index demonstrated a negative correlation with mortality rates, suggesting a potential inverse link between health outcomes and subjective well-being. Surprisingly, contrary to my initial assumptions, the analysis revealed minimal correlation between health indicators and the happiness index with economic factors like GDP. Looking for specific features, I discovered that countries such as Russia, characterized by high GDP but low life expectancy, and Germany, exhibiting relatively low immunization rates despite a high GDP, which underscore the complexity of these relationships across different countries. Additionally, the fluctuation of the happiness score over time is also relatively small.")

    st.write("**6.	What difficulties did you have in completing the project?**")
    st.write("The foremost difficulty I encountered in completing this project was the difficulty in sourcing suitable datasets, which often lacked the comprehensive information necessary for thorough analysis. Additionally, I found that scraping data from APIs also has some challenges. Furthermore, drawing conclusive insights from the data proved challenging, particularly given the intricate nature of the relationship between economic factors, health indicators, and the happiness index across countries. ")

    st.write("**7.	What skills did you wish you had while you were doing the project?**")
    st.write("I wish I had enhanced skills in data cleaning and modeling, and also I wish to know more tips for plotting and visualization techniques. In addition, I would wish to know more sophisticated analytical techniques, such as machine learning algorithms, that could offer deeper insights into the complex interplay between economic factors, health indicators, and the happiness index.")
    st.write("**8.	What would you do “next” to expand or augment the project?**")
    st.write("I will incorporate additional factors such as environmental indicators to provide a more comprehensive understanding of the determinants of national well-being. Additionally, I would like to integrate historical data across multiple years which will enable longitudinal analysis, facilitating the identification of trends and patterns over time. ")

def page_datasets():
    st.title("Datasets")
    st.write("**1. World GDP Data (Scrape-able) from Worldometers: https://www.worldometers.info/gdp/gdp-by-country/**")
    st.write("This data source offers a comprehensive insight into the economic landscape of various countries. This dataset includes essential metrics such as nominal GDP, GDP growth, population statistics, GDP per capita, and the share of world GDP. It provides valuable information to analyze and understand the economic performance and productivity levels across different nations.")
    
    st.write("**2. API Data - Country Health Indicators from RapidAPI's CountryStats Database:https://rapidapi.com/indiedevway/api/countrystats-database/**")
    st.write("The CountryStats APT serves as a rich repository of health indicators for countries worldwide, including immunization rates, mortality rates, prevalence of diseases such as diabetes and tuberculosis, life expectancy, and population growth rates. By integrating data from this source, we can gain deeper insights into public health outcomes and disparities across various regions and demographic groups.")
    
    st.write("**3. Happiness Index Data from Kaggle: https://www.kaggle.com/datasets/anas123siddiqui/happiness-index-data**")
    st.write("This dataset provides a longitudinal record of happiness index scores for countries spanning from 2016 to 2022. It offers a unique perspective on societal well-being and life satisfaction levels across different nations over a seven-year period, allowing for the exploration of correlations and patterns between economic factors, health indicators, and overall happiness levels.")


def page_main_app():
    st.title("Main App")


    selected_y_feature = st.sidebar.selectbox("Select Y-Axis Feature", ['Overall rank', 'Life expectancy', 'Immunization (%)', 'Score_2016', 'Score_2017', 'Score_2018', 'Score_2019', 'Score_2020', 'Score_2021', 'Score_2022'], index=3)
    selected_x_feature = st.sidebar.selectbox("Select X-Axis Feature", ['GDP per capita', 'GDP (nominal, 2022)', 'Life expectancy', 'Immunization (%)', 'Diabetes prevalence (% of population ages 20 to 79)', 'Mortality rate, under-5 (per 1,000 live births)'], index=2)
    selected_countries = st.sidebar.multiselect("Select Country(s)", df_combined['Country'].unique())

    gdp_range = st.sidebar.slider("GDP (nominal, 2022) range", 0.0, float(df_combined['GDP (nominal, 2022)'].max()), (0.0, float(df_combined['GDP (nominal, 2022)'].max())))


    if not selected_countries:  
        df_filtered = df_combined[df_combined['GDP (nominal, 2022)'] <= gdp_range[1]]
    else:
        df_filtered = df_combined[(df_combined['Country'].isin(selected_countries)) & (df_combined['GDP (nominal, 2022)'] <= gdp_range[1])]


    st.subheader("Filtered Data Table")
    st.write(df_filtered)


    st.subheader("Scatter Plot")
    fig_scatter = px.scatter(df_filtered, x=selected_x_feature, y=selected_y_feature, color='Country', hover_name='Country', title=f"{selected_x_feature} vs {selected_y_feature}")
    fig_scatter.update_layout(xaxis_title=selected_x_feature, yaxis_title=selected_y_feature)
    st.plotly_chart(fig_scatter)


    df_line = df_filtered[['Country', 'Score_2016', 'Score_2017', 'Score_2018', 'Score_2019', 'Score_2020', 'Score_2021', 'Score_2022']]
    df_line.set_index('Country', inplace=True)
    df_line = df_line.transpose()


    st.subheader("Happiness Scores Over Time")
    fig_line = px.line(df_line, x=df_line.index, y=df_line.columns, title="Happiness Scores from 2016 to 2022")
    fig_line.update_layout(xaxis_title="Year", yaxis_title="Happiness Score", legend_title="Country")
    st.plotly_chart(fig_line)


if __name__ == "__main__":
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Instruction", "Analysis", "Datasets", "Main App"])

    if selection == "Instruction":
        instruction()
    elif selection == "Analysis":
        page_conclusion()
    elif selection == "Datasets":
        page_datasets()
    else:
        page_main_app()

