import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)
# 一个类型：HTTPResponse 六个方法：read readline readlines getcode geturl getheaders

# response是HTTPResponse的类型
print(type(response))

# 按照一个字节一个字节的去读
content = response.read()
print(content)

# 读取一行
content = response.readline()
print(content)

# 读取多行
content = response.readlines()
print(content)

# 返回状态码
print(response.getcode())

# 返回的是url地址
print(response.geturl())

# 获取是一个状态信息
print(response.getheaders())