ans=[0]*200
n=0
while True:
    str=input().split()
    ans[int(str[0])]+=int(str[1])
    n=max(n,int(str[0]))
    if int(str[0])==0:
        break
while True:
    str=input().split()
    ans[int(str[0])]+=int(str[1])
    n=max(n,int(str[0]))
    if int(str[0])==0:
        break


#hello
ab=list(range(n+1))
ab.reverse()
flag1=0
flag=1
for i in ab:
    if ans[i]==0:
        continue
    if flag1==1 and ans[i]>0:
        print("+",end="")
        flag=0
    elif flag1==0:
        flag1=1
    if ans[i]!=1:
        print(ans[i],end="")
        flag=0
    if i!=0:
        print("x",end="")
        flag=0
    if i>1:
        print(i,end="")
        flag=0
if flag==1:
    print(0)