# setup work directory
os.chdir('.')
# download the WHO covid data as csv
wget.download('https://covid19.who.int/WHO-COVID-19-global-data.csv')
# get a panda dataframe shaped for the visualisation
covid_df_1 = fetch_covid_df()

# map plot
new_cases_figure = create_covid_choroplethmap(covid_df_1, 'New_cases', max_range=1000000)
cumulative_cases_figure = create_covid_choroplethmap(covid_df_1, 'Cumulative_cases', max_range=1000000)
new_deaths_figure = create_covid_choroplethmap(covid_df_1, 'New_deaths', max_range=10000)
cumulative_deaths_figure = create_covid_choroplethmap(covid_df_1, 'Cumulative_deaths', max_range=1000000)