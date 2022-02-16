import pandas as pd
from geopy.geocoders import Nominatim
def addingCor(contry):
    lon=[]
    lat=[]
    geo = Nominatim(user_agent="not-my-application")
    for i in contry:
        corr = geo.geocode(i)
        try:
            lon.append(corr.longitude)
            lat.append(corr.latitude)
        except:
            lon.append("None")
            lat.append("None")
    return lon,lat



src = pd.read_csv("./data/data_with_clusters.csv")
new_csv = src[["pays","cluster_km","cluster_km_2","cluster_km_5"]]
print("Wating assiging the contry coordinate...")
lon, lat = addingCor(new_csv["pays"])
new_csv = new_csv.assign(longitude=lon,latitude=lat)
print(new_csv.head())