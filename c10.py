# import urllib.request
# from bs4 import BeautifulSoup

'''if the web need to be logged in'''
# url = 'http://www.pythonchallenge.com/pc/return/bull.html'
# user = 'huge'
# password = 'file'
# pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# pwdmgr.add_password(None, url, user, password)

# auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
# opener = urllib.request.build_opener(auth_handler)
# content = opener.open(url).read()
# soup = BeautifulSoup(content, 'html.parser')
# co = soup('area')
# ll1 = co[0].get('coords')

a = ['1']
# creat a number series called look and say sequence.
while True:
	try:
		print(a[30])
		print(len(a[30]))
		break
	except:
		al = a[-1]
		nxal = ''
		lnum = list()
		lcount = list()
		for i in range(len(al)):
			if i == 0:
				lnum.append(al[i])
				lcount.append(1)
			elif al[i] == al[i-1]:
				lcount[-1] = lcount[-1]+1
			else:
				lnum.append(al[i])
				lcount.append(1)
		for i in range(len(lnum)):
			nxal = nxal + str(lcount[i]) + lnum[i]
		a.append(nxal)
