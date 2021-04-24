import requests
from bs4 import BeautifulSoup

postData = {
'_csrf': '20c811c0-8044-48b0-aa60-26de2ff45964',
'startStation': '1000-臺北',
'endStation': '4400-高雄',
'transfer': 'ONE',
'rideDate': '2021/04/24',
'startOrEndTime': 'true',
'startTime': '07:00',
'endTime': '08:00',
'trainTypeList': 'ALL',
'_isQryEarlyBirdTrn': 'on',
'query': '查詢'}

respond = requests.post('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime', data = postData)
soup = BeautifulSoup(respond.text)
data = soup.find_all('tr', class_ = 'trip-column')

for info in data:

    location = info.find_all('span', class_='location')
    location1 = location[0].text
    location2 = location[1].text
    
    time = info.find_all('td')
    time1 = time[1].text
    time2 = time[2].text
    time3 = time[3].text
    time4 = time[4].text

    print(location1, location2, time1, time2, time3, time4)
