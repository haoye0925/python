import requests
url='http://www.baidu.com/s?'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count += 1

if __name__ == "__main__":
    wds = ('hy','热门','华晨宇')
    baidu(wds)
f = open('res1.txt','r')
lines = f.readlines()
for line in lines:
    if "http" in lines:
        print(lines)