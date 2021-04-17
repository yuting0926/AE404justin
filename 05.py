import json
import requests

url = 'https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=30&before=235776614'
respond = requests.get(url)

jsonData = json.loads(respond.text)

D = {}
for data in jsonData:
    D['title'] = data['title']
    D['topics'] = data['topics']
    D['gender'] = data['gender']
    D['school'] = data['school']
    
    with open('Dcard.json', 'a', encoding='utf-8') as f:
        json.dump(D, f, ensure_ascii=False)