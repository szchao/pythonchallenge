import urllib.request
import re
from bs4 import BeautifulSoup, Comment
import bz2

htl = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read()
soup = BeautifulSoup(htl, 'html.parser')

comment = soup.find_all(string=lambda text: isinstance(text, Comment))

nap = re.findall("'(BZh.+)'", comment[0])

# conver byteslike string to bytes
# source: https://stackoverflow.com/questions/33257875/python-string-to-bytes-conversion-double-backslash-issue
un = nap[0].encode().decode('unicode-escape').encode('ISO-8859-1')
un = bz2.decompress(un)

pd = nap[1].encode().decode('unicode-escape').encode('ISO-8859-1')
pd = bz2.decompress(pd)

print('name:', un.decode())
print('password:', pd.decode())