import pandas as pd
import plotly.express as px


df = pd.read_csv("Tallinn_od_serie.csv")

# You can also visualize Estonia simplified od
# df = pd.read_csv("Estonia_od_serie.csv")



fig = px.line_mapbox(df, lat="lat", lon="lon", color="locations", zoom=15, height=300)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=6, mapbox_center_lat = 59.3550,
    margin={"r":0,"t":20,"l":0,"b":0},height=1200, width=1600,)

fig.show()