from bs4 import BeautifulSoup
import requests
import json

def get_link():
    request = requests.get("https://www.senscritique.com/films/tops/top111")
    soup = BeautifulSoup(request.text, 'lxml').find_all("h2", {'class': 'd-heading2 elco-title'})
    return [(link.find('a').get('href') + "/details") for link in soup]

def get_country(links):
    country_list = []
    for link in links:

        url = "https://www.senscritique.com/" + link

        #country = BeautifulSoup(requests.get(url).text, 'lxml').find('aside', {'class': 'd-grid-aside'}).find_all("ul")[0]
        country = BeautifulSoup(requests.get(url).text, 'lxml').find('aside', {'class': 'd-grid-aside'}).find_all("h4")
        f = [tag for tag in country if tag.text == "Pays d'origine"]
        x = f[0].find_next('ul')
        
        country_list.append(', '.join([element.text for element in x.find_all("li")]))

    return country_list

def merge(list1, list2):
    list1["country"] = list2
    return list1

def add_country_to_json(country_list):
    with open('Data/data_sc.json', 'r') as f:
        data = json.load(f)

    data = list(map(merge, data, country_list))
    print(data[0])

    with open('Data/test_sc.json', 'w') as f:
        json.dump(data, f, indent=1)


add_country_to_json(get_country(get_link()))