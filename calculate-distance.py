from json import load,dump
from pprint import pprint
from shapely.geometry import Polygon,Point
from itertools import chain
import sys

amtrak_json_file_name = 'rail.geojson'
amtrak_json_file = open(amtrak_json_file_name)

amtrak_json_data = load(amtrak_json_file)

amtrak_features = amtrak_json_data['features']

amtrak_stations = []

for amtrak_feature in amtrak_features:
    amtrak_point = Point(amtrak_feature['geometry']['coordinates'])
    amtrak_name = amtrak_feature['properties']['STN_NAME']
    amtrak_stations.append({'station_name':amtrak_name, 'coordinates':amtrak_point})

park_bureaus = ['nps', 'fs']

for park_bureau in park_bureaus:
    park_json_file = open(park_bureau + '.geojson')
    park_json_data = load(park_json_file)

    park_features = park_json_data['features']

    for park_feature in park_features:
        coordinates = chain.from_iterable(park_feature['geometry']['coordinates'])

        park_polygon = Polygon(map(tuple, coordinates))

        min_distance = sys.maxsize
        min_name = ""
        for amtrak_station in amtrak_stations:
            distance = park_polygon.distance(amtrak_station['coordinates'])

            if distance < min_distance:
                min_distance = distance
                min_name = amtrak_station['station_name']

            park_feature['properties']['title'] = park_feature['properties']['NAME1']
            park_feature['properties']['description'] = "Closest Station: " + min_name + "\n"
            park_feature['properties']['description'] = "Distance: " + (min_distance * 1000) + " miles"

    dump(park_json_data, open(park_bureau + '_with_stations.geojson', 'w'))
