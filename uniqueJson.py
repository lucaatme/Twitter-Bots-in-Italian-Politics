import json

politicians = ["EmmaBonino", "SilvioBerlusconi",
               "MatteoSalvini", "NicolaFratoianni", "GiuseppeConte"]

for politician in politicians:
    with open('preparsedFULL' + politician + '.json', 'r') as f:
        data = json.load(f)
        # remove duplicates based on user['user']['user_data']['id_str']
    data = list({v['user']['user_data']['id_str']: v for v in data}.values())

    with open('preparsedFULL' + politician + 'EDITED.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Done with " + politician)
