import json

# load all the results from botometer
full_botometer_results = []

for i in range(1, 15):
    with open('./emmaBonino/botometer_results_EmmaBonino' + str(i) + '.json') as f:
        full_botometer_results.append(json.load(f))

print("Done with Bonino")

for i in range(4, 140):
    with open('./giuseppeConte/Botometer_results_GiuseppeConte300' + str(i) + '00.json') as f:
        full_botometer_results.append(json.load(f))

print("Done with Conte")

for i in range(1, 197):
    with open('./matteoSalvini/botometer_results_MatteoSalvini' + str(i) + '00.json') as f:
        full_botometer_results.append(json.load(f))

print("Done with Salvini")

for i in range(1, 101):
    with open('./silvioBerlusconi/botometer_results_SilvioBerlusconi' + str(i) + '00.json') as f:
        full_botometer_results.append(json.load(f))

print("Done with Berlusconi")

for i in range(1, 31):
    with open('./nicolaFratoianni/botometer_results_NicolaFratoianni' + str(i) + '.json') as f:
        full_botometer_results.append(json.load(f))

print("Done with Fratoianni")

# open the txt file of interest
with open('./giuseppeConte/botsIdGiuseppeConte.txt') as f:
    # load each line as a string
    bots_id = [line.strip() for line in f]

object_to_output = []

for element in full_botometer_results:
    for user in element:
        if user['user']['user_data']['id_str'] in bots_id:
            object_to_output.append(user)

# output object_to_output in a json file
with open('preparsedFULLGiuseppeConte.json', 'w') as f:
    json.dump(object_to_output, f, indent=4)
