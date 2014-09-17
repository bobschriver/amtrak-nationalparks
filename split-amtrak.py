from json import load,dump
from pprint import pprint

json_file_name = 'amtrak.geojson'
json_file = open(json_file_name)

json_data = load(json_file)

features = json_data['features']

station_types = {}

for feature in features:
    station_type = feature['properties']['STNTYPE']

    if station_type not in station_types:
        feature_collection = {}
        feature_collection["type"] = 'FeatureCollection'
        feature_collection["features"] = []
        station_types[station_type] = feature_collection
            
    station_types[station_type]["features"].append(feature) 

for station_type,feature_collection in station_types.items():
    dump(feature_collection, open(station_type + '.geojson', 'w'))
