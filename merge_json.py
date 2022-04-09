import os
import json

"""
ne fonctionne pas pour moi
"""

def merge_json(first_file, second_file):

    with open(first_file, 'r') as file:
        first_json = json.loads(file.read())

    with open(second_file, 'r') as file:
        second_json = json.loads(file.read())

    for first_value, second_value in (first_json, second_json):
        if first_value['title'] == second_value['title']:
            first_value['results'][0].update(second_value['results'][0])

    with open('final_data.json', 'w') as json_file:
        json.dump(first_json, json_file, indent=1)
        print('Successfully appended to the JSON file')


#merge_json(os.path.abspath("IMDB/data.json"), os.path.abspath("data_sc.json"))



def merge_data(first_file, second_file):

    with open(first_file, 'r') as file:
        first_json = json.loads(file.read())

    with open(second_file, 'r') as file:
        second_json = json.loads(file.read())


    for i in range(100):
        first_json[i]["results"][0]["reviews sc"] = second_json[i]["results"][0]["reviews sc"]
        first_json[i]["results"][0]["rating sc"] = second_json[i]["results"][0]["rating sc"]

    with open('final_data.json', 'w') as json_file:
        json.dump(first_json, json_file, indent=1)
        print('Successfully appended to the JSON file')

merge_data("IMDB/data.json", "SensScrapFilmImdb/data_sc.json")