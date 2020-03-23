import plotly.express as px
import json
import pandas as pd

with open('saopaulo.json') as f:
    data = json.load(f)
geojson = data

df=pd.DataFrame(columns=geojson['features'][0]['properties'].keys())
for element in geojson['features']:
    df_temp =pd.DataFrame.from_dict(element['properties'])
    df=pd.concat([df,df_temp])

fig=px.bar(df,              # our dataframe
       x="nome",         # x will be the 'key' column of the dataframe
       y="perimetro_",   # y will be the 'doc_count' column of the dataframe
       title=f"Repurchase count per District",
       labels={"nome": "# District","perimetro_": "Repurchase count"}, # the axis names
       color_discrete_sequence=["blueviolet"], # the colors used
       height=500,
       width=800)
fig.show()
##py.iplot(data, filename='scatter-for-dashboard')

fig2=px.bar(df,              # our dataframe
       x="nome",         # x will be the 'key' column of the dataframe
       y="area_1",   # y will be the 'doc_count' column of the dataframe
       title=f"Average Courier Time per District",
       labels={"nome": "District","area_1": "Avg Courier Time(seconds)"}, # the axis names
       color_discrete_sequence=["blueviolet"], # the colors used
       height=500,
       width=800)

fig2.show()

fig3=px.bar(df,              # our dataframe
      x="nome",         # x will be the 'key' column of the dataframe
      y="area_1",   # y will be the 'doc_count' column of the dataframe
      title=f"Order cancellation per Restaurant",
      labels={"nome": "Restaurant","area_1": "Order Cancellation"}, # the axis names
      color_discrete_sequence=["red"], # the colors used
      height=500,
      width=800)

fig3.show()