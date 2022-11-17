import json

import jsonpath

obj = json.load(open('19、jsonpath.json','r',encoding = 'utf-8'))

# 书店所有书的作者
author = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author)

# 所有的作者
author_list = jsonpath.jsonpath(obj,'$..author')
print(author_list)

# store下面的所有元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)

# store下面所有的price
price_list = jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# 第三本书
book = jsonpath.jsonpath(obj,'$..book[2]')
print(book)

# 最后一本书
book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
print(book)

# 前两本书
book_list = jsonpath.jsonpath(obj,'$..book[:2]')
print(book_list)

# 过滤出所有包含ISBN的书
book_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(book_list)

# 过滤出所有超过10的书
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)