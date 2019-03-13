import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from bs4 import Comment
import re

content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()

soup = BeautifulSoup(content,"html.parser")

a = soup.find_all(string=lambda text: isinstance(text, Comment))

b = re.findall('[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]',a[0])

print(''.join(b))