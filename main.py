import requests
from send_email import send_email

topic = 'tesla'

api_key = 'f00bba79d5ec4c03946caf6db33b998b'
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'from=2024-04-22&'
       'sortBy=publishedAt&'
       'apiKey=f00bba79d5ec4c03946caf6db33b998b&'
       'language=en')

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

message = ''

# Access the articles titles and description
for article in content['articles'][:20]:
    title = article['title']
    description = article['description']
    try:
        message = ("Subject: Today's news" + '\n' + message + title + '\n'
                   + description + '\n' + article['url'] + 2*'\n')
    except TypeError:
        continue
message = message.encode('utf-8')
send_email(message)

