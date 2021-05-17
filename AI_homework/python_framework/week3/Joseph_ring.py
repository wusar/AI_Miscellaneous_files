
N=int(input())

monkey=list(range(N))

pos=0

while(len(monkey)!=1):
    pos=(pos+2)%(len(monkey))
    del monkey[pos]
    
    #print(len(monkey))
print(monkey[0]+1)

