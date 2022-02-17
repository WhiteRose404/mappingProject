from geopy.geocoders import Nominatim

def add_df_to_lan_lat_geojson(df, properties):
    geojson = {'type':'FeatureCollection', 'features':[]}
    geo = Nominatim(user_agent="not-my-application")
    for _, row in df.iterrows():
        try:
            corr = geo.geocode(row["pays"])
        except:
            continue
        feature = {'type':'Feature',
                   "color": "blue",
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [corr.latitude,corr.latitude]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


print("hvfjhvfuhbgjhbjk")

