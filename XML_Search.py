import urllib.request, urllib.parse, urllib.error
import Lib.xml.etree.ElementTree as ET
total = list()



fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_392340.xml").read()



tree = ET.fromstring(fhand)
lst = tree.findall('comments/comment')
for items in lst: total.append(items.find('count').text)
for num in range(0, len(total)):total[num] = int(total[num])

print(sum(total))