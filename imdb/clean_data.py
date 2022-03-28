import json
import sys, os

sys.path.insert(0, str(os.getcwd()) + '/TextAnalyzer')
print(os.getcwd())

from analyze import text_analyze

jFile = open("imdb/data.json")

data = json.load(jFile)

for i in range(0, len(data)):
    done = set()
    result_usr = []
    result_cr = []
    #for d in data[i]["results"][0]["critics reviews"]:
    for d in data[i]["results"]:
        for usr in d["users reviews"]:
            usr['nlp'] = text_analyze(usr["content"], 'en')
            result_cr.append(usr)
        data[i]["results"][0]["users reviews"] = result_cr
        for cr in d["critics reviews"]:
            if str(d.keys()) not in done:
                done.add(str(cr.keys()))
                print(str(cr.keys()))
                cr["nlp"] = text_analyze([*cr.values()][0], 'en')
                print()
                result_cr.append(cr)

        data[i]["results"][0]["critics reviews"] = result_cr

with open('data3.json', 'w') as jF:
    json.dump(data, jF, indent=1)