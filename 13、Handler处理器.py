# Handler 定制更高级的请求头 （随着业务逻辑的复杂 请求对象的定制已经满足不了我们的需求（动态cookie和代理））
import urllib.request

# 需求  使用Handler来访问百度  获取网页源码
url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

# Handler  build_opener  open

# (1)获取Handler对象
hander = urllib.request.HTTPHandler()

# (2)获取opener对象
opener = urllib.request.build_opener(hander)

# (3)调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)