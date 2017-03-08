from bs4 import BeautifulSoup
import requests

url = 'https://www.baidu.com.html'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data, 'lxml')
print(soup)
'''titles = soup.select('#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div > div > a > div > div > div > img')
print(titles)

#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(1) > div > div > div.item.name > a

'''


