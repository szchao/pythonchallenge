import difflib
f = open('deltas')
rl = list()
ll = list()
for line in f:
	ll.append(line[:53])
	rl.append(line[56:].strip())
d = difflib.Differ().compare(ll, rl)

f1 = open('f1.png', 'wb')
f2 = open('f2.png', 'wb')
f3 = open('f3.png', 'wb')

for line in d:
	data = line[2:].split()
	data = bytes([int(i, 16) for i in data])
	if line[0] == '+':
		f1.write(data)
	elif line[0] == '-':
		f2.write(data)
	else:
		f3.write(data)

f1.close()
f2.close()
f3.close()