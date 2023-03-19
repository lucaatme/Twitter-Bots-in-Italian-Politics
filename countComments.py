import json

politicians = ["EnricoLetta", "GiuseppeConte", "NicolaFratoianni",
               "GiorgiaMeloni", "SilvioBerlusconi", "MatteoSalvini"]

counter = 0

for politician in politicians:
    with open('results' + politician + '.json', 'r') as f:
        data = json.load(f)
        # remove duplicates based on user['user']['user_data']['id_str']
    data = list({v['id']: v for v in data}.values())
    # count the number of elements in the list
    counter += len(data)
    print("Done with " + politician)
    data = []

print("Total number of elements: ", counter)
