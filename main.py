import requests
from send_email import send_email

api_key = 'f00bba79d5ec4c03946caf6db33b998b'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-04-22&sortBy=publis\
hedAt&apiKey=f00bba79d5ec4c03946caf6db33b998b'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

message = ''

# Access the articles titles and description
for article in content['articles']:
    title = article['title']
    description = article['description']
    try:
        message = message + title + '\n' + description + 2*'\n'
    except TypeError:
        continue
message = message.encode('utf-8')
send_email(message)

