ss = "map"
s=list()
for i in ss:
	if ord(i)>=97 and ord(i)<=120:
		i = chr(ord(i)+2)
	elif i == 'y':
		i = 'a'
	elif i == 'z':
		i = 'b'
	s.append(i)
s= ''.join(s)
print(s)