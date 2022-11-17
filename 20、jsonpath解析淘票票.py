import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1668571809617_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ":authority": "dianying.taobao.com",
    # ":method": "GET",
    # ":path": "/cityAction.json?activityId&_ksTS=1668571809617_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true",
    # ":scheme": "https",
    # "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "bx-v": "2.2.3",
    "cookie": "cna=BxrxG6OuPGoCAdoTYIrmaj9P; _m_h5_tk=1648a850be59e31c0922b0507ab1fae5_1668225168050; _m_h5_tk_enc=ecca989877c170e45b28f9b2192cbd26; miid=921683885520609227; t=1df674255daa2f31f3ec4d11fb75b96a; xlly_s=1; cookie2=1f87d94c1011aa291212d202a7116e5e; v=0; _tb_token_=7563b98dee17b; tfstk=cYvGBuABLC518ckvRF6sFHn33-udZeyVrKJBLDYSEp5k6HJFisVUa9BsxN0S7S1..; l=eBOj89RITy4Hhp0fBOfwhurza77tMIRAguPzaNbMiOCP9FCe5fNRW6z-UDLwCnGVhs3JR3r0glSeBeYBqn4jjqj4axom4ADmn; isg=BJmZsKyYHnyFa8Ly15MVSLJXqIVzJo3YaTv44btOYEA_wrlUA3T_qFPUwIa0-iUQ",
    "referer": "https://dianying.taobao.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

# split 切割json
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('20、jsonpath解析淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('20、jsonpath解析淘票票.json','r',encoding = 'utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)