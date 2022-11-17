import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.starbucks.com.cn/menu/'
base_url = 'https://www.starbucks.com.cn/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

soup = BeautifulSoup(content,'lxml')

name_list = soup.select('ul[class="grid padded-3 product"] strong')
img_list = soup.select('ul[class="grid padded-3 product"] div')
names = list()
for name in name_list:
    names.append((name.get_text()))

imgs = list()
for img in img_list:
    img_url = base_url + str(img)[59:-10]
    imgs.append(img_url)

for i in range(len(imgs)):
    urllib.request.urlretrieve(url=imgs[i],filename=names[i]+'.jpg')
# （热/冷）  /要变