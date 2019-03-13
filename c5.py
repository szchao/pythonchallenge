import pickle
import urllib.request

content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
fhand = open('pickl.p', 'wb')
fhand.write(content)
fhand.close()

fhand = open('pickl.p', 'rb')
cc = pickle.load(fhand)
print(cc)
fhand.close()
