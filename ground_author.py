import json
import requests
import time
import nltk

WIKI_API_BASE_URL = "https://en.wikipedia.org/w/api.php"


def wikipedia_search(query):

    S = requests.Session()

    PARAMS = {
        'action': "query",
        'list': "search",
        'srsearch': query,
        'format': "json"
    }

    R = S.get(url=WIKI_API_BASE_URL, params=PARAMS)
    DATA = R.json()

    if len(DATA['query']['search']) > 0:
        return DATA['query']['search'][0]['title'], DATA['query']['search'][0]['pageid']
    else:
        return None, None


def wikipedia_get_url_from_pageid(pageid):
    S = requests.Session()

    PARAMS = {
        'action': "query",
        'prop': "info",
        'pageids': pageid,
        'inprop': "url",
        'format': "json"

    }

    R = S.get(url=WIKI_API_BASE_URL, params=PARAMS)

    DATA = R.json()
    return DATA["query"]["pages"]["{}".format(pageid)]["fullurl"]


def extact_author_name(description):
    toks = nltk.word_tokenize(description)
    if len(toks) <= 3:
        return None
    if toks[2].istitle():
        return " ".join(toks[:3])
    else:
        return " ".join(toks[:2])

if __name__ == '__main__':

    nltk.download('punkt')
    with open("nyt_rfd_raw.json") as fin:
        raw_rfd_json = json.load(fin)

    author_set = set()
    for article in raw_rfd_json:
        author_desc = article["debate_articles"]["author_description"]
        author_name = extact_author_name(author_desc)
        if author_name:
            author_set.add(author_name)

    print(author_set)
    print(len(author_set))
    print(len(raw_rfd_json))

