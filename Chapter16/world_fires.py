import os
import requests
import csv


os.chdir(os.path.dirname(__file__))
filename = 'test.csv'

try:
    with open(filename) as f:
        text = f.read()
    reader = csv.reader(text.strip().split('\n'))    
except FileNotFoundError:
    url = 'https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/' + \
        'MODIS_C6_Global_24h.csv'
    r = requests.get(url)
    with open(filename, 'w') as f:
        f.write(r.text)
    reader = csv.reader(r.text.strip().split('\n'))

header = next(reader)

lons, lats, bgts = [], [], []

for row in reader:
    try:
        lon = float(row[header.index('longitude')])
        lat = float(row[header.index('latitude')])
        bgt = float(row[header.index('brightness')])
    except ValueError:
        print(reader.line_num)
        # print(__exception__)
    else:
        lons.append(lon)
        lats.append(lat)
        bgts.append(bgt)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': bgts,
    'marker': {
        'size': [ (bgt-300)/5 for bgt in bgts ],
        'color': bgts,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='test.html')
