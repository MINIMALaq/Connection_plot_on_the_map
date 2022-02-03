import pandas as pd

estonia = pd.read_csv("Estonia_od_serie.csv")

import plotly.express as px

fig = px.line_mapbox(estonia, lat="lat", lon="lon", color="locations", zoom=3, height=300)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=6, mapbox_center_lat = 58,
    margin={"r":0,"t":20,"l":0,"b":0},height=1200, width=1600,)

fig.show()