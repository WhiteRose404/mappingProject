from geopy.geocoders import Nominatim
import pandas as pd
from Function import add_df_to_lan_lat_geojson

properties = ["pays","cluster_km"]
src = pd.read_csv("./data/data_with_clusters.csv")
print("Wating assiging the contry coordinate...")
geoJson = add_df_to_lan_lat_geojson(src, properties)