import requests
from bs4 import BeautifulSoup

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)

soup = BeautifulSoup(data.text)

divs = soup.find_all('div', class_='cover')

for each_divs in divs:
    img = each_divs['src']
    bookname = each_divs["alt"]
    
    sss = requests.get(img)    
    with open(bookname + ".jpg", "wb") as f:
        f.write(sss.content)
        

