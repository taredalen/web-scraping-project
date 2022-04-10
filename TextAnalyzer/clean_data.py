import os
import sys
import json

from TextAnalyzer.analyze import text_analyze

sys.path.insert(0, str(os.getcwd()) + '/TextAnalyzer')

def clean_data():
    jFile = open('../Data/final_data.json')

    data = json.load(jFile)

    for i in range(len(data)):
        nlp_review_user_list = []
        nlp_review_critiques_list = []
        nlp_review_sc_list = []

        for film_review in data[i]["results"][0]["users reviews"]:
            film_review["nlp"] = text_analyze(film_review["content"], 'en')
            nlp_review_user_list.append(film_review)
        data[i]["results"][0]["users reviews"] = nlp_review_user_list

        for film_review in data[i]["results"][0]["critics reviews"]:
            film_review["nlp"] = text_analyze(film_review["content"], 'en')
            nlp_review_critiques_list.append(film_review)
        data[i]["results"][0]["critics reviews"] = nlp_review_critiques_list

        for film_review in data[i]["results"][0]["reviews sc"]:
            film_review["nlp"] = text_analyze(film_review["content"], 'en')
            nlp_review_sc_list.append(film_review)
        data[i]["results"][0]["reviews sc"] = nlp_review_sc_list

        print(i, data[i]["title"])

    with open('../Data/final_data.json', 'w') as jF:
        json.dump(data, jF, indent=1)
        print('Successfully appended to the JSON file : final_data.json')

clean_data()