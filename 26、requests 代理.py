import requests
import random
url = 'https://www.baidu.com/s'

headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    "Cookie": "BIDUPSID=26609DEDE0BF6E398202B8CD2A198111; PSTM=1656755166; BAIDUID=26609DEDE0BF6E396BFAB503EF9F9B31:SL=0:NR=10:FG=1; BDUSS=BmU1ZFNzJ1aERjM3NOdGk0SFpZNGVuckJ-bVdXLUJmWjd-dE9sNUVTUXl3RE5qRVFBQUFBJCQAAAAAAAAAAAEAAAB12OxAMTU2cWF6NDQ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIzDGMyMwxjT3; BDUSS_BFESS=BmU1ZFNzJ1aERjM3NOdGk0SFpZNGVuckJ-bVdXLUJmWjd-dE9sNUVTUXl3RE5qRVFBQUFBJCQAAAAAAAAAAAEAAAB12OxAMTU2cWF6NDQ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIzDGMyMwxjT3; newlogin=1; BD_UPN=12314753; H_PS_PSSID=36542_37512_37687_37495_37778_37724_37797_36805_37532_37673_26350_22159; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=e9c6Feu2z%2F9gtFbVEOKV2%2Bq10Q0bI1MitZCOFw88CAxQegdaf57iHah7RSs; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=26609DEDE0BF6E396BFAB503EF9F9B31:SL=0:NR=10:FG=1; baikeVisitId=6bd37f1d-a96c-4e15-aab1-b7d540ce581d",
    # "Host": "www.baidu.com",
    # "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
}

data = {
    'wd':'ip'
}

porxys = [
    {'http':'27.42.168.46:55481'},
    {'http' :'121.13.252.62:41564'}
]
proxy = random.choice(porxys)
response = requests.get(url=url,params=data,headers=headers,proxies=proxy)

content = response.text

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)