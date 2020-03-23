# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Rappi Dashboard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='mapbox',
        fig = px.choropleth_mapbox(df, geojson=geojson, color='perimetro_',
                               locations="geocodigo", featureidkey="properties.geocodigo",
                               hover_data=['nome', 'area_1'],
                               hover_name='nome',
                               center={"lat": -23.5505, "lon": -46.625290},
                               mapbox_style="carto-positron"
                               )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


@app.callback(Output('mapbox', 'mapbox_choropleth'))
def update_graph():


    fig = px.choropleth_mapbox(df, geojson=geojson, color='perimetro_',
                               locations="geocodigo", featureidkey="properties.geocodigo",
                               hover_data=['nome', 'area_1'],
                               hover_name='nome',
                               center={"lat": -23.5505, "lon": -46.625290},
                               mapbox_style="carto-positron"
                               )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()
    return fig