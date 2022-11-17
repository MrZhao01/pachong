# urllib
# （1）一个类型以及六个请求
# （2）get请求
# （3）post请求
# （4）ajax的get请求
# （5）ajax的post请求
# （6）cookie登录
# （7）代理


# requests
# （1）一个类型以及六个属性
# （2）get请求
# （3）post请求
# （4）代理
# （5）cookie   验证码

import requests

url = 'https://www.google.com/search'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'q':'北京'
}
# url  请求资源路径   parmas参数    kwargs字典
response = requests.get(url=url,params=data,headers=headers)
content = response.text
print(content)
# 参数使用parmas传递
# 不需要编码