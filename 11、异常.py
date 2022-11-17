import urllib.request
import urllib.error

# HTTPError是指路径名称不对
# URLError是指主机地址问题
url = 'https://blog.csdn.net/sulixu/article/details/119818949'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级……')