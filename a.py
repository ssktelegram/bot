import urllib
import requests
key = 'fe5df5f79db41efb1b79be5befe337d0c8ea8'
def shorttheurl(url):
    r=f'http://cutt.ly/api/api.php?key={key}&short={url}'
    res=requests.get(r).json()['url']
    return res['shortLink']
    

abc=shorttheurl("https://amzn.to/3VKKIiC")
print(abc)