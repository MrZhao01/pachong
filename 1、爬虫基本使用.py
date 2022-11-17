import urllib.request

# 使用urllib爬取百度的源码
# (1)定义一个url  就是你要访问的地址    伪造浏览器请求头
url = 'http://www.baidu.com/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# （2）模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3)获取响应中的页面的源码
# read方法  返回的是字节形式的二进制数据
#  我们要将二进制的数据转成为字符串
#  二进制-->字符串   解码  decode('编码的格式')
content = response.read().decode('utf-8')

# (4)打印数据
print(content)