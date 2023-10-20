from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <meta charset="UTF-8">
        <title>我是網頁標題</title>
    </head>
    <body>
        <div>
            <p id="p1">我是段落一</p>
            <p id="p2" class='red'>我是段落二</p>
        </div>
    </body>
</html>
'''

sp = BeautifulSoup(html, "lxml")

print(sp.find('p'), end="\n\n")
print(sp.find_all("p"), end="\n\n")
print(sp.find("p", {"id":"p2", "class":"red"}), end="\n\n")
print(sp.find("p", id="p2", class_="red"), end="\n\n")
