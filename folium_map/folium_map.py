import folium
import os
import pandas
import webbrowser

DATA_FOLDER= os.path.join(os.path.dirname(__file__),'../data')
data = pandas.read_csv('{}/Volcanoes_USA.txt'.format(DATA_FOLDER))
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def url_producer(elev):
	if elev <= 0:
		raise ValueError('Volcanoe cannot be smaller than 1 metre!')
	elif elev < 1000:
		return 'icons/vol1.png'
	elif 1000 <= elev <= 3000:
		return 'icons/vol2.png'
	else:
		return 'icons/vol3.png'

def create_map():

	map = folium.Map(location=[33.8024176, 10.2871], zoom_start=6, tiles='Mapbox Bright')

	fgv = folium.FeatureGroup(name='Volcanoes')

	for lt, ln, el in zip(lat, lon, elev):
		icon = folium.features.CustomIcon(url_producer(el),
			icon_size=(40,40))
		fgv.add_child(folium.Marker(location=[lt, ln], popup=str(el)+'m', icon=icon))

	fgp = folium.FeatureGroup(name='Population')

	fgp.add_child(folium.GeoJson(data=open('{}/world.json'.format(DATA_FOLDER), 'r', encoding='utf-8-sig').read(),
		style_function=lambda x: {'fillColor': 'green' if  x['properties']['POP2005'] <= 1000000
		else 'orange' if x['properties']['POP2005'] <= 20000000 else 'red'}))

	map.add_child(fgv)
	map.add_child(fgp)
	map.add_child(folium.LayerControl())
	map.save('US-Volcanoes.html')
	webbrowser.open('US-Volcanoes.html', 2)