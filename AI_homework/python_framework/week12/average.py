s=0
count=0
a=0
while 1:
	a=int(input())
	if(a<0):
		break
	s+=a
	count+=1
ave=s/count
print(f"{ave:.2f}")


