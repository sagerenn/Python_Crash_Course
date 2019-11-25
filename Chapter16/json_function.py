import requests
import json
import os

os.chdir(os.path.dirname(__file__))

# URL = \
#     'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
# URL = \
#     'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson'
URL = \
    'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson'

r = requests.get(url = URL) 
data = r.json()

# filename = 'test.json'
# with open(filename, 'w') as f:
#     json.dump(data, f, indent=4)

# with open(filename) as f:
#     a = json.load(f)

# print(f"{data['metadata']['count']} {len(data['features'])}")
title = data['metadata']['title']
mags, lons, lats, hover_texts = [], [], [], []
for eq in data['features']:
    mags.append(eq['properties']['mag'])
    hover_texts.append(eq['properties']['title'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])

print(mags[:3], lons[:3], lats[:3])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from random import choice
from plotly import colors

colorscale = choice(list(colors.PLOTLY_SCALES.keys()))

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [ 5*mag for mag in mags ],
        'color': mags,
        'colorscale': colorscale,
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='test.html')

