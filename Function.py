from geopy.geocoders import Nominatim

def add_df_to_lan_lat_geojson(df, properties):
	geojson = {'type':'FeatureCollection', 'features':[]}
	geo = Nominatim(user_agent="not-my-application")
	for _, row in df.iterrows():
		feature = {'type':'Feature','color': 'blue','properties':{},'geometry':{'type':'Point','coordinates':[]}}
		corr = geo.geocode(row["pays"])
		feature['geometry']['coordinates'] = [corr.latitude,corr.longitude]
		for prop in properties:
			feature['properties'][prop] = row[prop]
			geojson['features'].append(feature)
		return geojson

