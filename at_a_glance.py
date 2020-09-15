import requests
import json

# https://wikimedia.org/api/rest_v1/#/

while True:
    var =input("Enter query below (or \"quit\" to quit):").strip()
    r=requests.get("/".join(["https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article","en.wikipedia.org","all-access", "all-agents",var,"monthly/20200101/20200909"]))
    if var=="quit":
        break
    print("last week of daily pageviews for ",var,":")
    try:
        for x in json.loads(r.content)["items"]:
            print (x["views"])
    except:
        print("Error occured while reading response")
