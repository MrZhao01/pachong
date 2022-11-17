import json

import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    "kw": "12"
}

# url  请求地址        data  请求参数       kwargs字典
response = requests.post(url,data=data,headers=headers)
content = response.text
content = json.loads(content)
print(content)

# 总结：
# （1）post请求不需要编解码
# （2）post请求的参数是data
# （3）不需要请求对象的定制
