import urllib.request, urllib.parse
import re
import bz2
import xmlrpc.client

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
cookieinfo = ''
nxnum = '12345'

while True:
	nexturl = url + nxnum
	data = urllib.request.urlopen(nexturl)
	content = data.read().decode()
	cookies = data.getheader('Set-Cookie')
	nxcookie = re.findall('info=(.+?);',cookies)[0]
	cookieinfo = cookieinfo + nxcookie
	try:
		nxnum = re.findall('and the next busynothing is ([0-9]+)',content)[0]
	except:
		break
# print(cookieinfo)

# cookieinfo = '''BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'''
# decode cookieinfo
cookieinfo = urllib.parse.unquote_to_bytes(cookieinfo.replace('+', '%20'))
info = bz2.decompress(cookieinfo).decode()
print(info)


proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
resp = proxy.phone('Leopold')
print(resp)
# this will print 555-VIOLIN

msg = 'the flowers are on their way'
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
rep = urllib.request.Request(url, headers={'Cookie': 'info='+urllib.parse.quote_plus(msg)} )
resp = urllib.request.urlopen(rep)
print(resp.read().decode())
