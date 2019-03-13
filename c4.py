import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'



content = urllib.request.urlopen(html).read()
soup = BeautifulSoup(content,"html.parser")
tag = soup('a')
back = tag[0].get('href')
html = 'http://www.pythonchallenge.com/pc/def/' + back


while True:
	content = urllib.request.urlopen(html).read().decode()
	try:
		num = re.findall('[0-9]+', content)[-1]
		a = html
		html = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?' + urllib.parse.urlencode({'nothing': num})
	except:
		print(content)
		if content == 'Yes. Divide by two and keep going.':
			html = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
			continue
		print(html)
		print(a)
		break

#content = urllib.request.urlopen('www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827').read().decode()