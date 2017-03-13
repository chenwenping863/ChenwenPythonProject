import requests
from bs4 import BeautifulSoup
from datetime import datetime
newsurl = 'http://news.sina.com.cn/china/'
res = requests.get(newsurl)
# print res.content

"""print (res.content)"""

"""DOM Tree
res.encoding = 'utf-8'"""

"""soup = BeautifulSoup(res)
print type(soup)
header = soup.select('h1')
print header"""

a = '<a href="#" qoo=123 abc=456>i am a link</a>'
soup = BeautifulSoup(res.content, 'html.parser')
"""print soup"""
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        print h2
        time = news.select('.time')[0].text
        print time
        a = news.select('a')[0]['href']
        print a
        print time, h2, a






