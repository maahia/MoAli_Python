import urllib.request

filehandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in filehandler:
    print(line.decode().strip())
