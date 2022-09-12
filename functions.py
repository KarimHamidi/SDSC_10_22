def fetch_covid_df():
    df = pd.read_csv('./WHO-COVID-19-global-data.csv')
# derivation of months and year from date :
    covid_df_1 = (df
              .assign(Date = lambda x: pd.to_datetime(x.Date_reported))
              .assign(Year = lambda y: y.Date.dt.year)
              .assign(Month = lambda z: z.Date.dt.month_name())
              .assign(YearnMonth = lambda w: w.Date.dt.strftime('%Y-%m'))
              .sort_values(['Country', 'YearnMonth'])
              .groupby(['Country', 'YearnMonth'],  sort=False)[['New_cases', 'Cumulative_cases', 'New_deaths',
                                                     'Cumulative_deaths']].apply(sum).reset_index())
    return covid_df_1

def create_covid_choroplethmap(df, var_of_interest:str, max_range:int):
    hexcode = 0
    colors = {'background': 'white',
              'text': 'black'}
    map = px.choropleth(df, locations='Country', locationmode='country names', color=var_of_interest,
                  hover_name='Country', color_continuous_scale='reds', range_color=[1, max_range],
                  title='', animation_frame='YearnMonth',
                  projection='natural earth')
    map.update_layout(
        margin={"r": 0, "t": 0, "l": 40, "b": 0},
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'])
    return map
