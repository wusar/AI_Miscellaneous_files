n=int(input())
a=input().split()

for i in range(n-1,-1,-1):
	flag=1
	for j in range(i,n):
		if a[j] not in a[0:i]:
			flag=0
			break
	if flag==0:
		break

print(i)

