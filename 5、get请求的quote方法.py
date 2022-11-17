# https://www.google.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 获取 https://www.google.com/search?q=周杰伦
import urllib.request
# unicode编码请求
import urllib.parse
name = urllib.parse.quote('周杰伦')

url = 'https://www.google.com/search?q='
url=url + name

#请求对象的定制是为了解决反爬的第一种手段
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url,headers=headers)

# 获取页面信息

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)