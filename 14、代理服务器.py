import urllib.request

url = 'https://www.baidu.com/s?tn=39042058_8_oem_dg&ie=utf-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

proxies = {
    'http' : '183.236.232.160:8080'
}

request = urllib.request.Request(url,headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)