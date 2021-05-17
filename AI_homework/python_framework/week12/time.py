time1=input().split()
time2=input().split()

shi=int(time2[0])-int(time1[0])
fen=int(time2[1])-int(time1[1]) 
if fen<0:
	fen+=60
	shi-=1
print(str(shi)+' '+str(fen))                                     




