import json
import urllib.request, urllib.parse, urllib.error
import ssl
tot = int()
url = 'http://py4e-data.dr-chuck.net/comments_392341.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
# print(data)
info = json.loads(data)
# print(info)
# print('User count:', len(info))
#
for item in info['comments']:
    tot = tot + item['count']

print(tot)
