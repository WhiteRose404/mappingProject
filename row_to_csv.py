import pandas as pd
from Function import add_df_to_lan_lat_geojson
import plotly.express as px

properties = ['pays','cluster_km', 'cluster_km_2', 'cluster_km_5']
src = pd.read_csv("./data/data_with_clusters.csv")[properties]
print("Wating assiging the contry coordinate...")
geoJson = add_df_to_lan_lat_geojson(src, properties)
print(geoJson)

