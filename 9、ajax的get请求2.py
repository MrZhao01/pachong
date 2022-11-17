import urllib.request
import urllib.parse

def create_request():
    base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"
    data = {
        'start': (page-1)*20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=headers)
    
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(page,content):
    with open(f'douban_{page}.json','w',encoding='utf-8') as fp:
        fp.write(content)

# 程序的入口
if __name__ == '__main__':
    start_page = int(input("请输入起始的页码："))
    end_page = int(input("请输入结束的页码："))

    for page in range(start_page,end_page+1):
# 每一页都有自己的请求对象定制
        request = create_request()
        content = get_content(request)
        download(page,content)