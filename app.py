import pandas as pd
import plotly.express as px
from pathlib import Path
import json

folder = Path.cwd() / "data"
df = pd.read_csv(folder / "Eng_data_with_clusters_f.csv")
with open(folder / "countries.geojson") as f:
    data = json.load(f)
    fig = px.choropleth_mapbox( df, geojson=data, color="cluster_km",
                                locations="pays",featureidkey="properties.ADMIN",
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()