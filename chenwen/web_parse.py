from bs4 import BeautifulSoup

with open('/Users/chenwenping/百度一下，你就知道.htm', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    print(Soup)
    # tb1 > tr:nth-child(1) > td
    images = Soup.select('#s_lg_img')
    titles = Soup.select()

for image in images:
    print(images.get_text('tb1 > tr:nth-child(1) > td'))

for image, title in zip(images, titles):
    data = {
        'title' : title.get_text(),
        'image': image.get_text(),
    }
    print(data)