import requests

api_key = "e8b7006263c0455484d3cd45aaf95e43"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-10-30&sortBy=publishedAt&apiKey=" \
      "e8b7006263c0455484d3cd45aaf95e43"

# make request
request = requests.get(url)

# get dictionary of articles
content = request.json()

# access articles and titles
for article in content["articles"]:
    print(article['title'])
    print(article["description"])
