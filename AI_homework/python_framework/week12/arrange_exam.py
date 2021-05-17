N,Q=input().split()
N=int(N)
Q=int(Q)
all_time=[]
for i in range(N):
    temp=input().split()
    for j in temp[1:]:
        all_time.append(int(j))

for i in range(101):
    b=all_time.count(i)
    if b>=Q:
        print(i)
        exit(0)

print(0)

