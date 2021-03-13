import requests
url = 'https://www.youtube.com/'

data = requests.get(url)
print(data.text)
