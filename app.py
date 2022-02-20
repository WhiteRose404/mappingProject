import pandas as pd
import plotly.express as px
from pathlib import Path
import json

folder = Path.cwd() / "data"
property = ["pays","cluster_km_2","cluster_km","cluster_km_5"]

ind = int(input("chose Your cluster \n" + ", ".join(property[1:]) + " :"))
print("Ploting...")
df = pd.read_csv(folder / "ENG_data_with_clusters_f.csv")[property]
with open(folder / "countries.geojson") as f:
    data = json.load(f)
    fig = px.choropleth_mapbox( df, geojson=data, color=property[ind],
                                locations="pays",featureidkey="properties.ADMIN",
                                mapbox_style="carto-positron",hover_data=["pays",property[ind]])
    print("Done")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.write_html( folder / (property[ind]+".html"))