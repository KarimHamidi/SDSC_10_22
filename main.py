# import and defined function needed
exec(open('./needed_imports.py').read())
exec(open('./functions.py').read())
exec(open('./data_prep.py').read())
## dashboard style
app = Dash(__name__)
# layout, maps and table
## allow cleanest map with no borders
hexcode = 0
colors = {'background': 'white',
          'text': 'black'}
borders = [hexcode for x in range(len(covid_df_1))]
# dashapp shaping
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Covid Pandemics new cases, deaths and evolution Globe wide 01.20 - 09.22.',
        style={'textAlign': 'center',
               'color': colors['text']}),
        html.Div(
            children='New cases monthly evolution',
            style={'textAlign': 'left',
                   'color': colors['text']}),
            dcc.Graph(id="nc_graph", figure=new_cases_figure.update_traces(marker_line_width=borders),
                      config={'displayModeBar': False},
                      style={"margin-top": "50px"}),
        html.Div(
            children='Cumulative cases monthly evolution',
            style={'textAlign': 'left',
                   'color': colors['text']}),
            dcc.Graph(id="cc_graph", figure=new_cases_figure.update_traces(marker_line_width=borders),
                      config={'displayModeBar': False},
                      style={"margin-top": "50px"}),
        html.Div(
            children='New deaths monthly evolution',
            style={'textAlign': 'left',
                   'color': colors['text']}),
            dcc.Graph(id="nd_graph", figure=new_deaths_figure.update_traces(marker_line_width=borders),
                      config={'displayModeBar': False}),
        html.Div(children='Cumulated deaths over months',
            style={'textAlign': 'left', 'color': colors['text']}),
            dcc.Graph(id="cd_graph", figure=cumulative_deaths_figure.update_traces(marker_line_width=borders),
                      config={'displayModeBar': False},
                      style={"margin-top": "50px"}),
        html.Div(children='Covid-19 infection and deaths evolution table',
                 style={'textAlign': 'left',
                       'color': colors['text']}),
                 dash_table.DataTable(covid_df_1.to_dict('records'),
                                      [{"name": i, "id": i} for i in covid_df_1.columns],
                                      filter_action='native',
                                      page_size=10,
                                      style_data={
                                          'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                                          'overflow': 'hidden',
                                          'textOverflow': 'ellipsis',
                                      }
                 )
])
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)