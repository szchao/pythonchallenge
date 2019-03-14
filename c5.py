import pickle
import urllib.request

content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
cc = pickle.loads(content)

# cc为一个list，每个item也是一个list，每个list下若干个元组，
#每个元组有两个数据，第一个为需要打印的字符，第二个为需要打印的个数。

for item in cc:
	for i in item:
		print(i[0]*i[1], end = '')
	print()