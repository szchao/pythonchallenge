import urllib.request
from PIL import Image
import io

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
user = 'huge'
password = 'file'

pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, url, user, password)

auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)
imgfile = opener.open(url).read()

imgfile = io.BytesIO(imgfile)
img1 = Image.open(imgfile)




img = img1.copy()
# solution 1:
pixels = img.load()
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if (i+j) % 2 != 0:
			pixels[i, j] = (0,0,0)
img.show()

# solution 2:
# odd = Image.new(img.mode, img.size)
# even = Image.new(img.mode, img.size)
# for i in range(img.size[0]):
# 	for j in range(img.size[1]):
# 		if (i+j)%2 ==0:
# 			odd.putpixel((i//2,j//2), img.getpixel((i,j)))
# 		else:
# 			even.putpixel((i//2,j//2), img.getpixel((i,j)))

# odd.show()
# even.show()

















