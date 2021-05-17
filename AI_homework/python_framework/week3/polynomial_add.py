
poly={}

flag=0

while True:
    exponential,coefficient=map(int,input().split())
    if exponential in poly.keys():
        poly[exponential]=poly[exponential]+coefficient
    else:
        poly[exponential]=coefficient
    if exponential==0:
        flag+=1
    if flag==2:
        break
poly=dict(sorted(poly.items(),key=lambda x:x[0],reverse=True))

print(poly)

i=0

for key in poly.keys():
    if i==0:
        if key==0:
            print(str(poly[key]),end='')
        elif poly[key]==1:
            print('x'+str(key),end='')
        else:
            print(str(poly[key])+'x'+str(key),end='')
    elif key==0 and poly[key]!=0:
        print('+'+str(poly[key]),end='')
    elif poly[key]==1:
        print('+'+'x'+str(key),end='')
    elif poly[key]>0:
        print('+'+str(poly[key])+'x'+str(key),end='')
    elif poly[key]<0:
        print(str(poly[key])+'x'+str(key),end='')
    
    i=1