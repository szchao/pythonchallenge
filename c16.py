from PIL import Image
import urllib.request
import io

# the codes blow should working but it didn't, It show error: AttributeError: 'GifImageFile' object has no attribute 'read'

# url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
# user = 'huge'
# password = 'file'

# pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# pwdmgr.add_password(None, url, user, password)

# auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
# opener = urllib.request.build_opener(auth_handler)
# imgfile = opener.open(url).read()
# imgfile = io.BytesIO(imgfile)
# mozart = Image.open(imgfile)s

# so first download mozart.gif.

img = Image.open('mozart.gif')
pixels = img.load()
new = Image.new(img.mode, img.size)
npixels = new.load()
w, h = img.size

for y in range(h):
	ll = 0
	for rred in range(w):
		if pixels[rred, y] == 195:
			break
	for x1 in range(rred, w):
		npixels[ll, y] = pixels[x1,y]
		ll = ll + 1
	for x2 in range(0, rred):
		npixels[ll, y] = pixels[x2,y]
		ll  = ll + 1
new.show()
