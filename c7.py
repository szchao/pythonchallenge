from PIL import Image
import urllib.request, io

# read image direct from the url.
imghand = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
imgfile = io.BytesIO(imghand)

lst = list()
img = Image.open(imgfile)
w, h = img.size

for wd in range(0, w):
	piva = img.getpixel((wd, h/2))
	if piva[0]==piva[1]==piva[2]:
		lst.append(piva[0])



#the first gray block has 5 pixles, others have 7 pixles, 
#first print the chr(piva), then print the rest.
print(chr(lst[0]), end = '')
for i in range (6,len(lst),7):
	print(chr(lst[i]), end = '')
print()

# the answer is smart guy, you made it. 
# the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
	print(chr(i), end = '')
print()