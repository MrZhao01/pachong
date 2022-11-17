import urllib.request
from lxml import etree

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

tree = etree.HTML(content)
name_list = tree.xpath('//strong/text()')
for name in name_list:
    print(name)
