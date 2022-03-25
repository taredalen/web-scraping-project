from bs4 import BeautifulSoup
import requests
import json
import time


def get_reviews(url, name):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    reviews = soup.find_all("a", {"class": "tracked-offsite-link" })
    filter = ["Roger Ebert", "ReelViews", "Washington Post", 
            "1,001 Movies Reviewed Before You Die", "1,001 Movies Reviewed Before You Die", "rogerebert.com",
            "New York Times"]
    review_list = []
    for review in reviews:
        for filt in filter:
            if filt in review.text:
                time.sleep(2)
                req = requests.get(review.get("href"))
                site = BeautifulSoup(req.text, "lxml")
                para = site.find_all("p")
                text_review = ""
                for text in para:
                    text_review += text.text
                review_list.append({review.text.strip(): text_review})

    return {name : review_list}

data = get_reviews("https://www.imdb.com/title/tt0025316/externalreviews?ref_=tt_ov_rt", "new york - miami")

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=1)
"""
    print(reviews[i].get("href"))
    req = requests.get(reviews[i].get("href"))
    review = BeautifulSoup(req.text, "lxml")
    para = review.find_all("p")
    text_review = ""
    for text in para:
        text_review += text.text

    print(text_review)
"""