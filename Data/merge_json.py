import os
import json

def merge_json(first_file, second_file):

    with open(first_file, 'r') as file:
        first_json = json.loads(file.read())

    with open(second_file, 'r') as file:
        second_json = json.loads(file.read())

    for first_value in first_json:
        for second_value in second_json:
            if first_value['title'] == second_value['title']:
                first_value['results'][0].update(second_value['results'][0])

    with open('final_data.json', 'w') as json_file:
        json.dump(first_json, json_file, indent=1)
        print('Successfully appended to the JSON file')

merge_json(os.path.abspath('Data/data_imdb.json'), os.path.abspath('Data/data_sc_imdb.json'))