# apikey=  1e5a955f17-994510bad0-r099up

import requests

api_key = '1e5a955f17-994510bad0-r099up'


############fetch-all
"""
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

"""
#################fetch one
"""
url = f'https://api.fastforex.io/fetch-one?api_key={api_key}'

querystring = {"from":"USD","to":"UZS"}

headers = {"Accept":"application/json"}

res=requests.request(method='GET',url=url,headers=headers,params=querystring)

resj = res.json()
print(resj['base'])
print(resj['result'])
print(resj['updated'])

"""

##################fetch multi
"""
url = f'https://api.fastforex.io/fetch-multi?api_key={api_key}'

querystring = {"from":"USD","to":"UZS,EUR,RUB"}

headers = {"Accept":"application/json"}

res = requests.get(url, headers=headers, params=querystring)
resj = res.json()

print(resj['base'])
print(resj['results'])
print(resj['updated'])
"""

##############fetch convert
"""

url = f'https://api.fastforex.io/convert?api_key={api_key}'

querystring = {"from":"USD","to":"UZS","amount":"100"}

headers = {"Accept":"application/json"}

res = requests.get(url=url, headers=headers, params=querystring)

resj = res.json()

print(resj['base'])

"""

###########currencies
"""

url = f'https://api.fastforex.io/currencies?api_key={api_key}'

headers = {"Accept":"application/json"}

res = requests.get(url=url, headers=headers)

resj = res.json()

print(resj['currencies']['AED'])
"""

##############usage

url = f'https://api.fastforex.io/usage?api_key={api_key}'

headers = {"Accept":"application/json"}

res = requests.get(url=url, headers=headers)

resj = res.json()

print(resj['usage'])