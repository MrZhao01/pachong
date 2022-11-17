import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# 因为urlopen方法中不能存储字典

url = 'https://www.baidu.com'

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
print(content)