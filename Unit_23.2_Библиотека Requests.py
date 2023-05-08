import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # делаем запрос на сервер по переданному адресу
texts = json.loads(r.content)
print(type(texts))
for text in texts:
    print(text[:50],'\n')