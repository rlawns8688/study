#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.16
# modified date  :   2024.02.16
# description  :

# import requests
import requests
url = 'https://api.github.com/some/endpoint'
r = requests.get(url)
data = {'re':'rerrrr',"gg":'ererer'}
# r.json()
url2 = 'https://httpbin.org/get'
# r_payload = requests.get(url2, params='payload')
r_put = requests.get(url2, json=data)
new = r_put.json()
print(new,r_put)
# r.json()
# r_payload.json()
# response = requests.head(url) # HEAD
# print("Status Code:", r_payload.status_code) #
# for header, value in r_payload.headers.items():
#     print(f"{header}: {value}")

# print(r_payload.json())
#

if __name__ == '__main__':
    pass
