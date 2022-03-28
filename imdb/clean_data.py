import json
from TextAnalyzer.analyze import text_analyze

jFile = open("imdb/data.json")

data = json.load(jFile)

for i in range(0, 1):
    done = set()
    result = []
    #for d in data[i]["results"][0]["critics reviews"]:
    
    for d in data[i]["results"][0]["critics reviews"]:
        if str(d.keys()) not in done:
            done.add(str(d.keys()))
            print(str(d.keys()))
            d["nlp"] = text_analyze([*d.values()][0], 'en')
            print()
            result.append(d)
    data[i]["results"][0]["critics reviews"] = result
    print(len(result))