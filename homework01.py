import urllib.request

def Search(word):
    param = urllib.parse.urlencode({'wd':word},encoding)
    url = 'http://www.baidu.com/s?'+param
    response=urllib.request.urlopen(url)
    HTML = response.read().decode('utf8')
    print(HTML)
if __name__ == "__main__":
    post('name','你真聪明！')


def post(word1,word2):
    url = 'http://httpbin.org/post'
    data = urllib.parse.urlencode({word1:word2},encoding='utf8')
    data = bytes(data,encoding='utf8')
    response = urllib.request.urlopen(url,data=data)
    print(response.read().decode('utf8'))
if __name__ == "__main__":
    post('name','你真聪明')
