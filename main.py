import requests
from send_email import send_email

topic = "tesla"
api_key = "e8b7006263c0455484d3cd45aaf95e43"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2022-10-30&sortBy=publishedAt&apiKey=" \
      "e8b7006263c0455484d3cd45aaf95e43&" \
      "language=en"

# make request
request = requests.get(url)

# get dictionary of articles
content = request.json()

email_content = {}

message = ""
# access articles and titles
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = "Subject: Today's news" + "\n"\
                  + message + article["title"] + "\n" + article["description"] + "\n"\
                  + article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)
