from json import load,dump
from pprint import pprint

json_file_name = 'federal.geojson'
json_file = open(json_file_name)

json_data = load(json_file)

features = json_data["features"]

pprint(features[0])

bureaus = {}

for feature in features:
    bureau = feature["properties"]["AGBUR"]
    
    if bureau != None:
        if bureau not in bureaus:
            bureaus[bureau] = open(bureau + '.geojson', 'w')
       
        dump(feature, bureaus[bureau])
        bureaus[bureau].write('\n')


