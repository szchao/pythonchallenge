import re
import zipfile

zp = zipfile.ZipFile('channel.zip')

content = zp.read('90052.txt').decode()
comment = zp.getinfo('90052.txt').comment.decode()

while True:
	try:
		num = re.findall('[0-9]+', content)
		num = num[0]
	except:
		# print(content)
		break
	content = zp.read(num + '.txt').decode()
	comment = comment + zp.getinfo(num + '.txt').comment.decode()

print(comment)

