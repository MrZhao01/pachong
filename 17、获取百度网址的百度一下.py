import urllib.request
from lxml import etree

# (1)获取网页的源码
# (2)解析    解析的服务器响应的文件   etree.html
# (3)打印

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析服务器响应的文件
tree = etree.HTML(content)

# 路径可以在浏览器中的Xpath获取
result = tree.xpath('//input[@id = "su"]/@value')[0]
print(result)