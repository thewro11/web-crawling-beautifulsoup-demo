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

sp = BeautifulSoup(html, 'lxml')
print(sp.select('title'), end="\n\n")
print(sp.select('p'), end="\n\n")
print(sp.select('#p1'), end="\n\n")
print(sp.select('.red'), end="\n\n")
