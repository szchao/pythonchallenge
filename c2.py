import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from bs4 import Comment
import re

content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()

soup = BeautifulSoup(content,"html.parser")

a = soup.find_all(string=lambda text: isinstance(text, Comment))

b = re.findall('[a-zA-Z0-9]+',a[1])

print(''.join(b))