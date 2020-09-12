import requests

url = 'http://127.0.0.1:8000/backend/stock/del/'
url2 = 'http://127.0.0.1:8000/backend/morder/del/'

item = {'moID': 'mo12'}

res = requests.post(url2, item)
print(res.text)

