from geopy.geocoders import Nominatim

def add_df_to_lan_lat_geojson(df, properties):
    geojson = {'type':'FeatureCollection', 'features':[]}
    geo = Nominatim(user_agent="not-my-application")
    find = 0
    for _, row in df.iterrows():
        lat,lon = 0,0
        feature = {'type':'Feature', 'properties':{}, 'geometry':{'type':'Point','coordinates':[]}}        
        try:
            corr=geo.geocode(row["pays"])
            lat,lon = corr.latitude,corr.longitude
        except :
            print("the api didnt find ", row["pays"])
            find+=1
            continue
        feature['geometry']['coordinates'] = [lat,lon]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    print(f"didnt find {find}")
    return geojson

