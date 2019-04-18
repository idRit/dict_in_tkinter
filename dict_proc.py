import requests
import json
import pprint

app_id = ""
app_key = ""
language = "en-gb"

def define(word=None):
    if word is None:
        return None

    word_id = word

    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

    oxford_dict = r.json()
    if "results" not in oxford_dict:
        return None

    list_of_dicts = []

    #definations
    for i in oxford_dict["results"]:
        for j in i["lexicalEntries"]:
            for k in j["entries"]:
                for v in k["senses"]:
                    pprint.pprint(v["definitions"])
                    list_of_dicts.append(v["definitions"])

    return list_of_dicts
