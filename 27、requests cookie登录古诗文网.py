# 通过登录  然后进入到主界面

# 通过找登录接口我们发现   登录的时候需要的参数很多
# __VIEWSTATE: f1St8oUeUQMh1qTjiIwIIPc3N4rbNCqS6IN8sXoLiOd1Ul3SVFikvmDVTdX7+BGZmXpAsyjzXkLM1i1SR1GZpY8uinzviv/yLM74vkSByN1tMj+Dq9dON/PYLLSxeQN8BMXt1V9BHeFeKT102J+JPAhr7FI=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 12345678901
# pwd: 1231111
# code: wy20
# denglu: 登录

# 我们观察得到__VIEWSTATE     __VIEWSTATEGENERATOR   code是一个可以变化的量

# 难点（1）__VIEWSTATE     __VIEWSTATEGENERATOR     一般情况下  看不到的数据都是在源码中
#     我们观察到这两个数据在页面的源码中，所以我们需要获取源码 然后解析
#    （2）验证码
import chaojiying
import requests
# import urllib.request
from bs4 import BeautifulSoup

login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# 获取页面的源码
response = requests.get(login_url,headers=headers)
content = response.text

soup = BeautifulSoup(content,'lxml')
__VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
__VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
url = 'https://so.gushiwen.cn' + code
# 获取了验证码的图片之后  下载到本地  然后观察验证码  观察之后   然后在控制台输入验证码  就可以将值给code
# urllib.request.urlretrieve(url,filename='验证码.jpg')
# requests里面有一个方法  session()  通过session的返回值  就能使用请求变成一个对象

session = requests.session()
# 验证码的url内容
response_code = session.get(url)
# 注意此时要使用二进制数据   因为我们要使用的图片的下载
content_code = response_code.content
# wb的模式就是将二进制写入文件
with open('验证码.jpg','wb')as fp:
    fp.write(content_code)

code_name = chaojiying.code

data = {
    "__VIEWSTATE": __VIEWSTATE,
    '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email":"12345678901",
    "pwd":"123456",
    "code":code_name,
    "denglu":"登录"
}

response_post = session.post(login_url,headers=headers,data = data)
response_post.encoding='utf-8'
content_post = response_post.text

with open('古诗文.html','w',encoding='utf-8')as fp:
    fp.write(content_post)

# 难点
# (1)隐藏域
# （2）验证码