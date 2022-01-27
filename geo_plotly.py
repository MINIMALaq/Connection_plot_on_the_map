# https://plotly.com/python/lines-on-maps/
import plotly.graph_objects as go
import pandas as pd

city = pd.read_csv('points.csv')
city.head()

od = pd.read_csv('od.csv',nrows = 2000)
od.head()

fig = go.Figure()


lons = []
lats = []
import numpy as np
lons = np.empty(3 * len(od))
lons[::3] = od['start_lon']
lons[1::3] = od['end_lon']
lons[2::3] = None
lats = np.empty(3 * len(od))
lats[::3] = od['start_lat']
lats[1::3] = od['end_lat']
lats[2::3] = None

print(len(lats))

fig.add_trace(
    go.Scattergeo(
        lon = lons,
        lat = lats,
        mode = 'lines',
        line = dict(width = 1,color = 'red'),
        opacity = 0.25
    )
)


fig.add_trace(go.Scattergeo(
    lon = city['lng'],
    lat = city['lat'],
    hoverinfo = 'text',
    text = city['name'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

fig.update_layout(
    title_text = 'March 2018 Estonia Origin Destination Matrice <br>',
    showlegend = False,
    geo = go.layout.Geo(
        scope = 'europe',
        # projection_type = 'van der grinten3',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
    height=700,
)

fig.show()
