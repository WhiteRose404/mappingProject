from urllib.request import urlopen
from googletrans import Translator

import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("./data/ENG_data_with_clusters_f.csv")

import plotly.express as px
f = open("./data/countries.geojson")
data = json.load(f)
#translator = Translator(service_urls=[
#     'translate.google.com','translate.google.fr'
#   ])
#translator = Translator(from_lang="French",to_lang="English")
#for i in df.index:
#    result = translator.translate(df.pays[i],dest='en',src='fr')
#    df.pays[i] = result.text
#    print(df.pays[i])

#df.to_csv('./data/ENG_data_with_clusters_f.csv')
#print(df.pays)
fig = px.choropleth_mapbox(df, geojson=data, color="cluster_km",locations="pays", featureidkey="properties.ADMIN",mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

f.close()