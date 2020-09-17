import requests
import json
import joblib
import wikipedia as wiki

# https://wikimedia.org/api/rest_v1/#/
fname="previous.jbl"
try:
    words=joblib.load(fname)
except:
    print("Setting up new file")
    words={}

while True:
    query =input("Enter query below (or \"quit\" to quit):").strip()
    page = wiki.search(query)[0]
    r=requests.get("/".join(["https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article","en.wikipedia.org","all-access", "all-agents",page,"monthly/20200101/20200909"]))
    if query=="keys":
        print(list(words.keys()))    
    elif query=="quit":
        break

    else:
        print("last week of daily pageviews for ",page,":")
        words[page]={}
        words[page]["viewslist"]=[]
        words[page]["query"]=query
        try:
            for item in json.loads(r.content)["items"]:
                words[page]["viewslist"].append(item["views"])
            print(words[page]["viewslist"])
        except:
            print("Error occured while reading response")
        joblib.dump(words,fname)
        
