from lxml import etree
import urllib.request

def creat_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/meinvxiezhen.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            "Cookie": "cz_statistics_visitor=68c7dfb8-f86b-1996-e149-c4fce4682d97; __bid_n=1847b2cd2e17179b4e4207; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1668513846; FPTOKEN=30$U511VMlaknaNT68/5ibzA76cK4qYYNJnpR78TYZiLJu4kq5NlW4pFko8o/I1xX8Gitc3UXNdkV2XXbp8Gtj/sVR5uz8O/8jlzeD9yxwi5n5lS1iANuG6k03gaxXYaJbOuR5Hc5VPuxc3YlSw0ZE5W+L5YA7FNHjdsVkZfrYdzHVRQUe2LCIeuXAf+HlTNJ7M4trBnlFzjJCxSoTB5mYaw7aQZjXCiOSYQl1rtj/sRVJAA4EHz2/yrOj6F06/ToCQqPSXzYjNbOWYBPa/nbaLFVqzEqJ1EV2Ju5TLvIXTeY3gTYzXc+4ORA5gwOgUNVc7VZsJtO9vKuB7o70MPseuXQ9j0f0L/MNTDy54FBh35zTfsqqbrWq7MYhrqVpaaEe+|kukes0ccpIQFU5K9r8jKD3LlBjVjymD9cErcyPya6RM=|10|ec1e45d71fabbdac8e5f7f5b63c142e8; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1668514287"
        }
        request = urllib.request.Request(url,headers=headers)
        return request

    else:
        url = f'https://sc.chinaz.com/tupian/meinvxiezhen_{page}.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            "Cookie": "cz_statistics_visitor=68c7dfb8-f86b-1996-e149-c4fce4682d97; __bid_n=1847b2cd2e17179b4e4207; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1668513846; FPTOKEN=30$U511VMlaknaNT68/5ibzA76cK4qYYNJnpR78TYZiLJu4kq5NlW4pFko8o/I1xX8Gitc3UXNdkV2XXbp8Gtj/sVR5uz8O/8jlzeD9yxwi5n5lS1iANuG6k03gaxXYaJbOuR5Hc5VPuxc3YlSw0ZE5W+L5YA7FNHjdsVkZfrYdzHVRQUe2LCIeuXAf+HlTNJ7M4trBnlFzjJCxSoTB5mYaw7aQZjXCiOSYQl1rtj/sRVJAA4EHz2/yrOj6F06/ToCQqPSXzYjNbOWYBPa/nbaLFVqzEqJ1EV2Ju5TLvIXTeY3gTYzXc+4ORA5gwOgUNVc7VZsJtO9vKuB7o70MPseuXQ9j0f0L/MNTDy54FBh35zTfsqqbrWq7MYhrqVpaaEe+|kukes0ccpIQFU5K9r8jKD3LlBjVjymD9cErcyPya6RM=|10|ec1e45d71fabbdac8e5f7f5b63c142e8; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1668514287"
        }
        request = urllib.request.Request(url,headers=headers)
        return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(content):
#     下载图片
    tree = etree.HTML(content)
    name_list = tree.xpath('//div/img/@alt')
    img_list = tree.xpath('//div/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        img = img_list[i]
        url = 'http:'+ img
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')



if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码：："))

    for page in range(start_page,end_page+1):
        request = creat_request(page)
        content = get_content(request)
        download(content)