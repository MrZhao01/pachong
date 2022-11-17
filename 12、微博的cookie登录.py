# 适用的场景：数据采集的时候 需要绕过登录
# 个人信息页面是utf-8 但是还报错了编码错误  因为并没有进入到个人信息页面  而是跳转到登录页面
import urllib.request

url ='https://weibo.com/u/6632654132/home?wvr=5'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'cookie' : ''
}
request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weobo.html','w',encoding='utf-8') as fp:
    fp.write(content)