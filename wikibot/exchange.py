# apikey=  1e5a955f17-994510bad0-r099up

import requests

api_key = '1e5a955f17-994510bad0-r099up'
# res = requests.get(url=f'https://api.fastforex.io/fetch-all?api_key={api_key}')
# print(res.json())
headers = {"Accept":"applicaton/json"}
url = f'https://api.fastforex.io/fetch-all?api_key={api_key}'

res=requests.request(method='GET',url=url,headers=headers)

json_res = res.json()

print(json_res['base'])
# print(json_res['results'])
print(json_res['updated'])
print(json_res['ms'])



