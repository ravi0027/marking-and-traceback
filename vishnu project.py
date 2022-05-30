import time
process1=0
process2=0
process3=0
in1=[1,2,7,0,0]#the interface through which the packet enter"""
out1=[250,10,200,220,10]#""""the interface through which the packet out"""
pm1=0
pm2=0
n=500
H=[[0]*n for i in range(n)]

def marking():
    global pm1,pm2,H
    R=0
    i=0
    j=0
    while(R<5):
    	x=in1[i]                                                                
    	y=pm1^pm2
    	H[x][y]=pm1
    	pm11=pm1
    	pm1=x
    	pm2=y^out1[j]
    	print(f"R:{R:<5}",end='\t') #R value
    	print(f"Iin:{in1[i]:<5}",end='\t') #in value
    	print(f"Iout:{out1[j]:<5}",end='\t') #out value
    	print(f"Bef P.Mark1:{pm11:<5}",end='\t')#before marking p.mark1
    	print(f"A.X value:{x:<5}",end='\t')#after marking p.mark1
    	print(f"Bef Y value:{y:<5}",end='\t')#before marking p.mark2
    	print(f"Aft P.Mark2:{pm2:<5}",end='\t')#after marking p.mark2
    	print(f"H[{x}][{y}]:{H[x][y]:<5}",end='\n') #hash value
    	R=R+1
    	i=i+1
    	j=j+1

def traceback():
    global pm1,pm2
    R=4
    i=4
    while(R>=0):
        Iout=pm1
        x=pm1
        y=pm2^out1[i]
        pm1=H[x][y]
        pm21=pm2
        pm2=y^pm1
        print(f"R:",R,end='\t') #R value
        print(f"Iin: {out1[i]:<5}",end='\t') #in value
        print(f"Iout: {Iout:<5}",end='\t') #out value
        print(f"Bef X value:{x:<5}",end='\t') #before x value
        print(f"H[{x}][{y}]:{H[x][y]:<5}",end='\t') #hash value                                                  
        print(f"Bef P.Mark2:{pm21:<5}",end='\t')# before pmark2 value
        print(f"Aft P.Mark2:{y:<5}",end='\n') #after pmark2 value
        R=R-1
        i=i-1

print("An Enhanced Packet Marking And Traceback Algorithm For IP Traceback...")
processtime=int(input("Enter value:"))
start=time.time()
while(process2<processtime):
    marking()
    process2=process2+1
end=time.time()
print("Time_taken for Marking:\n",end-start)
start=time.time()
while(process3<processtime):
    traceback()
    process3=process3+1
end=time.time()
print("Time_taken for Traceback:\n",end-start)
