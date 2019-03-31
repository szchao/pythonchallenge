from PIL import Image
import urllib.request
import io

# get the image from web
url = 'http://www.pythonchallenge.com/pc/return/wire.png'
user = 'huge'
password = 'file'

pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, url, user, password)
auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)

img = opener.open(url).read()

imgfile = io.BytesIO(img)
img = Image.open(imgfile)

pixlist = list(img.getdata())
new = Image.new(img.mode, (100,100))
pixels = new.load()
# for j in range(100):
# 	for i in range(100):
# 		pixels[i,j] = pixlist[0]
# 		del pixlist[0]
# new.show() 
# this will show 'bit', but it's not the answer.

j = 0
count = 0
while True:
	try:
		pixlist[0]
		for i in range(0+count, 100-count):
			pixels[i,j] = pixlist[0]
			del pixlist[0]
		for j in range(1+count, 100-count):
			pixels[i,j] = pixlist[0] 
			del pixlist[0]
		for i in range(98-count, -1+count, -1):
			pixels[i,j] = pixlist[0] 
			del pixlist[0]
		for j in range(98-count, 0+count, -1):
			pixels[i,j] = pixlist[0] 
			del pixlist[0]
		count = count + 1
	except:
		break
new.show()