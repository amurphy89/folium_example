import folium
import os
import pandas
import webbrowser

DATA_FOLDER = os.path.join(os.path.dirname(__file__), '../data')


def url_producer(elev):
    '''
    A function to return the URL of an image of a volcano
    based on elevation height.

     Parameters:
        elev (int): The height of a volcano.

     Raise:
        ValueError: If elevation parameter is 0 or less.

     Returns:
        str: A URL to an image of a volcano.

    '''
    if elev <= 0:
        raise ValueError('Volcanoe cannot be smaller than 1 metre!')
    elif elev < 1000:
        return 'icons/vol1.png'
    elif 1000 <= elev <= 3000:
        return 'icons/vol2.png'
    else:
        return 'icons/vol3.png'


def create_map():
    '''
    A function that creates and opens a folium map.

    This function reads volcanoe data using Pandas from a CSV.
    It then creates a Map object wwhich then adds a set of markers
    which show the location and elevation level of volcanoes in the USA.
    Then GeoJson is data is used to map population levels to countries.
    The map is then saved to HTML and opened in a default web browser.

    '''

    data = pandas.read_csv('{}/Volcanoes_USA.txt'.format(DATA_FOLDER))
    lat = list(data['LAT'])
    lon = list(data['LON'])
    elev = list(data['ELEV'])

    map = folium.Map(location=[33.8024176, 10.2871],
                     zoom_start=6, tiles='Mapbox Bright')

    fgv = folium.FeatureGroup(name='Volcanoes')

    for lt, ln, el in zip(lat, lon, elev):
        icon = folium.features.CustomIcon(url_producer(el),
                                          icon_size=(40, 40))
        fgv.add_child(folium.Marker(location=[lt, ln],
                                    popup=str(el)+'m', icon=icon))

    fgp = folium.FeatureGroup(name='Population')

    world_data = open('{}/world.json'.format(DATA_FOLDER), 'r',
                      encoding='utf-8-sig').read()

    fgp.add_child(folium.GeoJson(data=world_data,
                                 style_function=lambda x:
                                 {'fillColor': 'green'
                                  if x['properties']['POP2005'] <= 1000000
                                  else 'orange'
                                  if x['properties']['POP2005'] <= 20000000
                                  else 'red'}))

    map.add_child(fgv)
    map.add_child(fgp)
    map.add_child(folium.LayerControl())
    map.save('US-Volcanoes.html')
    webbrowser.open('US-Volcanoes.html', 2)
    