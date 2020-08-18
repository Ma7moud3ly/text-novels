import json
import requests
import sys
s=open("novels.json","r").read()
j=json.loads(s)

for i in range(0,len(j),1):
    id=j[i]['id']
    url=j[i]['url']
    url='http://www.blindarab.info/read/story-txt/'+url
    r=requests.get(url)
    if(r.apparent_encoding=='MacCyrillic'):r.encoding='cp1256'
    else:r.encoding='utf-8'
    dest="novels/%d.txt"%id
    open(dest,"w",encoding="utf-8").write(r.text)
    print(id)

quit()
