
n=int(input())
a=n
factor=[]

while 1:
	flag=1
	for i in range(2,n+1):
		if(n%i==0):
			flag=0
			factor.append(i)
			n=int(n/i)
			break	 
	if flag:
		break
print(str(a)+'=',end='')
for i in factor[0:-1]:
	print(str(i)+'*',end='')
print(factor[-1],end='')

