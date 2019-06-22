import urllib.request
url='https:www.17k.com/chapter/2933095/36699279.html'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
HTML = response.read().decode('utf8')
with open('c:/User/Administrator/Desktop/hy.txt','w',encoding='utf8') as y:
    y.write(HTML)