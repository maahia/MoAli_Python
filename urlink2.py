from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
lst = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_392338.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
x = str(soup.findAll("span"))
x = (re.findall('[0-9]+', x))
for num in range(0, len(x)):x[num] = int(x[num])
print(sum(x))




