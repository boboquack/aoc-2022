s=INPUT
pos=set()
d={'U':(0,1),'L':(-1,0),'R':(1,0),'D':(0,-1)}
tx=0
ty=0
hx=0
hy=0
for i in s.split('\n'):
    j,k=i.split()
    for _ in range(int(k)):
        a,b=d[j]
        hx+=a
        hy+=b
        if ty==hy+2:
            ty=hy+1
            tx=hx
        if ty==hy-2:
            ty=hy-1
            tx=hx
        if tx==hx+2:
            ty=hy
            tx=hx+1
        if tx==hx-2:
            ty=hy
            tx=hx-1
        pos.add((tx,ty))
print(len(pos))
pos=set()
d={'U':(0,1),'L':(-1,0),'R':(1,0),'D':(0,-1)}
lx=[0]*10
ly=[0]*10
#s='''R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2'''
for i in s.split('\n'):
    j,k=i.split()
    for _ in range(int(k)):
        a,b=d[j]
        lx[0]+=a
        ly[0]+=b
        for i in range(9):
            if ly[i+1]==ly[i]+2 and lx[i+1]==lx[i]+2:
                ly[i+1]=ly[i]+1
                lx[i+1]=lx[i]+1
            if ly[i+1]==ly[i]+2 and lx[i+1]==lx[i]-2:
                ly[i+1]=ly[i]+1
                lx[i+1]=lx[i]-1
            if ly[i+1]==ly[i]-2 and lx[i+1]==lx[i]+2:
                ly[i+1]=ly[i]-1
                lx[i+1]=lx[i]+1
            if ly[i+1]==ly[i]-2 and lx[i+1]==lx[i]-2:
                ly[i+1]=ly[i]-1
                lx[i+1]=lx[i]-1        
            
            if ly[i+1]==ly[i]+2:
                ly[i+1]=ly[i]+1
                lx[i+1]=lx[i]
            if ly[i+1]==ly[i]-2:
                ly[i+1]=ly[i]-1
                lx[i+1]=lx[i]
            if lx[i+1]==lx[i]+2:
                ly[i+1]=ly[i]
                lx[i+1]=lx[i]+1
            if lx[i+1]==lx[i]-2:
                ly[i+1]=ly[i]
                lx[i+1]=lx[i]-1
        pos.add((lx[-1],ly[-1]))
        #print(j)
        #print(lx)
        #print(ly)
print(len(pos))
