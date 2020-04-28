

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
url = "http://py4e-data.dr-chuck.net/known_by_Eugene.html"
i = 7
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print(url)
for i in range(i):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    #print("current url is", url)
    url = tag[17]
    url = url.get('href', None)
    print("the next url is", url)






# Retrieve all of the anchor tags
# tag = soup('a')
# url2 = tag[3]
# url2 = url2.get('href', None)
# html = urllib.request.urlopen(url2, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# print(url2)
