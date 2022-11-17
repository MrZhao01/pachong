# urlencode应用场景：多个参数的时候
import urllib.request
import urllib.parse
# https://www.baidu.com/s?wd=周杰伦&sex=男

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex' : '男',
    'location' : '中国台湾'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# data数据编码
new_data = urllib.parse.urlencode(data)

url = base_url + new_data

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)