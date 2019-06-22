import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
lines = HTML.split('\n')
for url in lines:
    try:
        response = requests.get(url,timeout=2)
        content = response.content
        conten2 = str(content)
        if '\\x' in conten2:
            print(conten2)
    except Exception as P:
        print(P)
        with open('%s,jpg','wb') as f:
            f.write(HTML.content)





import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808' 
response = requests.get(url)
HTML=response.text
URLS=HTML.split('\n')
lines=HTML.split('\n')

for line in lines:
    if '<a href' in lines:
        split_=line.split('http://')
        for i in line:
            if 'http' in i:
                url=i.split('','')[1]
                if 'jpg' in url:
                    URLS.append(url)
for url in URLS:
    response = requests.get(url)
    content1=response.content
    name= url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content1)
