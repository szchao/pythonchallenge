import urllib.request
url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
user = 'huge'
password = 'file'

pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, url, user, password)

auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)
data = opener.open(url).read()

for i in range(5):
	fhand = open(str(i)+'.jpg', 'wb')
	fhand.write(data[i::5])
	fhand.close()
 
 # answer is disproportional