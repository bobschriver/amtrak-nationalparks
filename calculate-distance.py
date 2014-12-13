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
bureau_colors = ['#006600', '#3333ff']

for park_bureau,bureau_color in zip(park_bureaus, bureau_colors):
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

	if park_feature['properties']['NAME1'] is not None :
		park_name = park_feature['properties']['NAME1']
	else :
		park_name = ""

	park_feature['properties'] = {}
	
	park_feature['properties']['description'] = park_name + "<br>"
        park_feature['properties']['description'] += "Closest Station: " + min_name + "<br>"
	    
	park_distance = "{:.2f}".format(min_distance * 100)
        park_feature['properties']['description'] += "Distance: " + park_distance + " miles"

	# Mapbox style information 
	park_feature['properties']['width'] = 1
	park_feature['properties']['fillColor'] = bureau_color
	park_feature['properties']['fillOpacity'] = 0.8

    dump(park_json_data, open(park_bureau + '_with_stations.geojson', 'w'))
