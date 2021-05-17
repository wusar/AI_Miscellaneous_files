
def gcd(x,y): 
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1,smaller + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd= i
	return gcd
origin=input()
origin=origin.split('/')
top=int(origin[0])
bottom=int(origin[1])

temp=gcd(top,bottom)
top=int(top/temp)
bottom=int(bottom/temp)
print(str(top)+'/'+str(bottom))

