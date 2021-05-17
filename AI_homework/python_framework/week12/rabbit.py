
n=int(input())
rabbits=[]
rabbits.append(0)
for i in range(n):
	for r in range(len(rabbits)):
		if rabbits[r]>0 and rabbits[r]<4:
			rabbits.append(0)
		rabbits[r]+=1
print(len(rabbits))
0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025