
#read input
firstline=["student id","name"]
pos={}
grades=[]
temp1=2
while 1:
    origin=list(input())
    if origin==["E","N","D"]:
        break;
    people=["","",""]
    ind=0
    for i in range(len(origin)):
        if origin[i]==",":
            ind+=1
            continue
        elif origin[i]==" " and origin[i-1]==",":
            continue
        people[ind]+=origin[i]
    if ind==1:
        flag=0
        for k in range(len(grades)):
            if grades[k][0]==people[0]:
                grades[k][1]=people[1]
                flag=1
                break
        if flag==0:
            grades.append(people)
    elif ind==2:
        if people[1] not in pos:
            pos[people[1]]=temp1
            temp1+=1
        flag=0
        for k in range(len(grades)):
            if grades[k][0]==people[0]:
                while len(grades[k])<temp1:
                    grades[k].append("")
                grades[k][pos[people[1]]]=float(people[2])
                flag=1
                break
        if flag==0:
            grades.append([people[0]])
            while len(grades[len(grades)-1])<temp1:
                grades[len(grades)-1].append("")
            grades[len(grades)-1][pos[people[1]]]=float(people[2])
for i in range(len(grades)):
    for k in range(len(grades)-1):
        if grades[k][0]>grades[k+1][0]:
            temp=grades[k]
            grades[k]=grades[k+1]
            grades[k+1]=temp
pos["special_flagaverage"]=temp1
temp1+=1
for i in range(len(grades)):
    while len(grades[i])<temp1:
        grades[i].append("")
    sum_num=0.0
    cur_num=0
    for k in range(temp1):
        if k<2:
            continue
        if grades[i][k]!="":
            sum_num+=float(grades[i][k])
            cur_num+=1
    if cur_num>0:
        grades[i][temp1-1]=(sum_num/cur_num)

ava=[-1]*(temp1)
alnum=0
allsco=0.0
for k in range(temp1-1):
    if k<2:
        continue
    stu_num=0
    num_sum=0.0
    for i in range(len(grades)):
        if grades[i][k]!="":
            stu_num+=1
            num_sum+=float(grades[i][k])
    if stu_num!=0:
        ava[k]=num_sum/stu_num
        allsco+=ava[k]
        alnum+=1
if alnum!=0:
    ava[temp1-1]=allsco/alnum

#print grades
print("student id, name",end="")
pos=sorted(pos.items())

for (i,k) in pos:
    if i=="special_flagaverage":
        print(", average",end="")
    else:
        print(", "+i,end="")
print("")

for i in range(len(grades)):
    print(grades[i][0]+", "+grades[i][1],end="")
    for (k,l) in pos:
        print(", ",end="")
        if grades[i][l]!="":
            print(round(float(grades[i][l]), 1),end="")
    print()
    

print(", ",end="")
for (k,l) in pos:
    print(", ",end="")
    print(round(ava[l], 1),end="")