import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import json
import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly' +
    '/datasets/master/2011_february_us_airport_traffic.csv')

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div([
    html.Div(
        html.Pre(id='lasso', style={'overflowY': 'scroll', 'height': '100vh'}),
        className="three columns"
    ),

    html.Div(
        className="nine columns",
        children=dcc.Graph(
            id='graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    },
                    'margin': {
                        'l': 0, 'r': 0, 'b': 0, 't': 0
                    },
                }
            }
        )
    )
], className="row")





@app.callback(
    Output('lasso', 'children'),
    [Input('graph', 'selectedData')])
def display_data(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)