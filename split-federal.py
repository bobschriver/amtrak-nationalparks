from json import load,dump
from pprint import pprint



json_file_name = 'federal.geojson'
json_file = open(json_file_name)

json_data = load(json_file)

features = json_data["features"]

bureaus = {}

for feature in features:
    bureau = feature["properties"]["AGBUR"]
    state = feature["properties"]["STATE"]

    print(feature)

    if bureau != None and state != None and state != 'AK' and state != 'HI':
        if bureau not in bureaus:
            feature_collection = {}
            feature_collection["type"] = 'FeatureCollection'
            feature_collection["features"] = []
            bureaus[bureau] = feature_collection
            
        bureaus[bureau]["features"].append(feature) 

for bureau,feature_collection in bureaus.items():
    dump(feature_collection, open(bureau + '.geojson', 'w'))
