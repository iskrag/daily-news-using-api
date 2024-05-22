import requests

api_key = 'f00bba79d5ec4c03946caf6db33b998b'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-04-22&sortBy=publis\
hedAt&apiKey=f00bba79d5ec4c03946caf6db33b998b'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the articles titles and description
for article in content['articles']:
    print(article['title'])