import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    "Cookie": "BAIDUID_BFESS=FCCE877A4F57C1D672E9A268564FA021:FG=1; __bid_n=18456ae46173ac4e7d4207; RT='z=1&dm=baidu.com&si=ebuk7tm7qw&ss=laaoi1tm&sl=4&tt=zw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1tj0&ul=24an&hd=24ay'; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=FCCE877A4F57C1D672E9A268564FA021; PSTM=1668334331; BA_HECTOR=0h852k0h850g2g8k01a50q2h1hn1gnv1e; ZFY=8vhDw8nIy9QsF8Pr:ABwbwkzav0BrksPhehUeDGRYM5A:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1668329908,1668401858; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1668401878; ab_sr=1.0.1_OGMwZjVlOTAzYmE5NDI5MWM0YmY0ZWZjMDUxYTlhOGI2OTcxNGEzNThkZjI1ZmI4ODQ0YWE1MzU2OWRhNDVlNjViMzJkYjI1YTkyMDliZGJhMjZmOWJiOGQ2YjU2NjRiZjBmMGE1ODM1ZGViNjJmZjc4ZmNiMmVjYzEyZThkMjY0OTIwNDgzMzY5ODIzNzNhYTRiNTBkMTVmODQ5NWUyYQ==",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}

data = {
    "from": "en",
    "to":"zh",
    "query "  : "hello",
    "simple_means_flag" :"3",
     "sign ":"54706.276099",
     "token" : "8b3b32ce7334a7349f61081dee3a379e",
   "domain ":"common",

}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url,data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)