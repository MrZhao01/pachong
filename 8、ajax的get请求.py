import urllib.request
import urllib.parse

m,n = map(int,input('请输入从第几部到第几部的内容：（空格隔开）').split())
m = m-1

# get请求
# 获取豆瓣电影第一页的数据，并且保存起来

url = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={m}&limit={n}'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('douban.json','w',encoding='utf-8') as fp:
    fp.write(content)
