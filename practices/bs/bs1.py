import requests
from bs4 import BeautifulSoup

url = "https://scholars.ncu.edu.tw/zh/persons/chia-yu-lin"
html = requests.get(url)
html.encoding = "UTF-8"
sp = BeautifulSoup(html.text, "lxml")

print(sp.title, end="\n\n")
print(sp.title.text, end="\n\n")
print(sp.h1, end="\n\n")
print(sp.p, end="\n\n")
