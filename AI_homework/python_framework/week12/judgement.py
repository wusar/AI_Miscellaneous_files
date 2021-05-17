
origin_score=input().split(' ')
score=[]
for i in range(len(origin_score)):
	score.append(int(origin_score[i]))
n=int(input())
for i in range(n):
	x=int(input())
	score[x]+=10
for i in range(len(score)):
	print(score[i],end=' ')
	

