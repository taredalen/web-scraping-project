import os
import sys
import json

from TextAnalyzer.analyze import text_analyze

sys.path.insert(0, str(os.getcwd()) + '/TextAnalyzer')

from TextAnalyzer import analyze

jFile = open('../Data/data_imdb_nlp.json')

data = json.load(jFile)
"""
for i in range(0, len(data)):
    done = set()
    result_usr = []
    result_cr = []
    #for d in data[i]["results"][0]["critics reviews"]:
    for d in data[i]["results"]:
        result_cr = []
        for usr in d["users reviews"]:
            usr['nlp'] = text_analyze(usr["content"], 'en')
            result_cr.append(usr)
        data[i]["results"][0]["users reviews"] = result_cr
        result_cr = []
        for cr in d["critics reviews"]:
            if str(d.keys()) not in done:
                done.add(str(cr.keys()))
                cr["nlp"] = text_analyze([*cr.values()][0], 'en')
                result_cr.append(cr)
        data[i]["results"][0]["critics reviews"] = result_cr
    print(i, data[i]["title"])

with open('IMDB/data3.json', 'w') as jF:
    json.dump(data, jF, indent=1)
"""

for i in range(1):
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


with open('../Data/data_imdb_nlp.json', 'w') as jF:
    json.dump(data, jF, indent=1)