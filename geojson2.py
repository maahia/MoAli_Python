import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = 42


serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = 'Illinois State University Joliet Junior College'


parms = dict()
parms['address'] = address
parms['key'] = api_key
# print(parms)
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
print(uh)
data = uh.read().decode()
# print(data)
# print('Retrieved', len(data), 'characters')
js = json.loads(data)
print(js)
print(js['results'][0]['place_id'])
# print(json.dumps(js, indent=4))

# lat = js['results'][0]['geometry']['location']['lat']
# lng = js['results'][0]['geometry']['location']['lng']
# print('lat', lat, 'lng', lng)
# location = js['results'][0]['formatted_address']
# print(location)