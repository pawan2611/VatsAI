import requests as req, time, json
from speak import say

def news():
    url=("https://newsapi.org/v2/top-headlines?country=in&apiKey=6f8f3438adca4df38c33f280159e6b07")
    news=req.get(url).text
    news=json.loads(news)
    news=news["articles"]
    i=0
    for i in news:
        say(i["title"])
        print(i["title"])
        print(i["url"]+"\n")
        time.sleep(0.5)

news()