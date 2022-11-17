from  lxml import etree
# xpath解析
# (1)本地文件                                             etree.parse
# (2)服务器响应的数据 response.read().decode('utf-8')      etree.HTML()

# xpath解析本地文件
tree = etree.parse('16、xpath.html')

# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# 查找所有有id的属性的标签
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为1的li标签  id后面的值要加引号
li_list = tree.xpath('//ul/li[@id="1"]/text()')

# 查找到id为li标签的class的属性值
# li = tree.xpath('//ul/li[@id="1*"]/@class')

# 查询id中包含l的li标签
li_list = tree.xpath("//ul/li[contains(@id,'c')]/text()")

# 查询id的值以1开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 查询id为l1 和 class为c1的标签
li_list = tree.xpath('//ul/li[@id= "l1" and @class = "c1"]/text()')

# li_list = tree.xpath('//ul/li[@id = "l1"]/text() | //ul/li/[@id = "l2"]/text()')
# 判断列表的长度
print(li_list)
print(len(li_list))