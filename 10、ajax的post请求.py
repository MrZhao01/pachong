import urllib.request
import urllib.parse

def creat_request():
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex": page,
        "pageSize": "10"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(base_url,data=data,headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(page,content):
    with open(f'KFC_{page}.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_pageIndex = int(input("请输入起始页数："))
    end_pageIndex = int(input("请输入结束页数："))

    for page in range(start_pageIndex,end_pageIndex+1):
        # 请求对象定制
        request = creat_request()
        # 获取网页源码
        content = get_content(request)
        # 下载
        download(page,content)