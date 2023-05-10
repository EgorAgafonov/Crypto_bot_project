import requests
import json
import lxml.html
from lxml import etree
                                            # Request запросы:

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url']) # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

# Таким образом мы можем удобно превращать данные, полученные из ответа JSON, в объекты структур данных Python
# с помощью библиотеки JSON, и удобно работать с ними.

                                            # Post запросы:

# r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
#
# print(r.content) # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет
#
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост запрос, но только
# # в этот раз тип передаваемых данных будет JSON
#
# print(r.content)

# request_API = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(request_API.content)
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50],'\n')

                                        # 23.4 Парсинг данных с сайтов

# 1.
# html = requests.get('https://www.python.org/').content
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')
# print(title)

# 2.
import requests
import json
import lxml.html
from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    print(a.text)

