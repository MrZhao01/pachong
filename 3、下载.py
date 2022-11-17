import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
#
# urllib.request.urlretrieve(url_page,'baidu.html')
# 下载图片
url_img = 'https://s-lol-web.op.gg/static/images/site/home/2022img_index_02_en@2x.png?v=1668149208300'
urllib.request.urlretrieve(url_img,filename='test.jpg')
# 下载视频
url_mp4 = ''
urllib.request.urlretrieve(url_mp4)