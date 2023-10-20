import requests

url = "http://www.ehappy.tw/demo.htm"
r = requests.get(url)
print(r.status_code)

if r.status_code == requests.codes.ok:
    print(r.text)
