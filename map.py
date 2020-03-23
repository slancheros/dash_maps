import json
import plotly.express as px
import pandas as pd

with open('saopaulo.json') as f:
    data = json.load(f)
geojson = data

df=pd.DataFrame(columns=geojson['features'][0]['properties'].keys())

for element in geojson['features']:
    df_temp =pd.DataFrame.from_dict(element['properties'])
    df=pd.concat([df,df_temp])

fig = px.choropleth_mapbox(df, geojson=geojson, color='area_1',
                    locations="geocodigo", featureidkey="properties.geocodigo",
                    hover_data=['nome','perimetro_'],
                    hover_name='nome',
                    center={"lat": -23.5505, "lon": -46.625290},
                    color_continuous_scale="Viridis",
                    mapbox_style="carto-positron"
                   )
fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



