s=INPUT

l=[]
for i in s.split():
    x,y,z=i.split(',')
    x,y,z=map(int,[x,y,z])
    l.append((x,y,z))
d=0
for i1,i2,i3 in l:
    for j1,j2,j3 in l:
        if abs(i1-j1)+abs(i2-j2)+abs(i3-j3)==1:d+=1
print(6*len(l)-d)

b=[[[False for i in range(51)] for i in range(51)] for i in range(51)]
for x,y,z in l:
    b[x][y][z]=True
q=[(0,0,0)]
v=set()
t=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
while len(q):
    x,y,z=q.pop()
    if (x,y,z) in v:continue
    b[x][y][z]=-1
    v.add((x,y,z))
    for dx,dy,dz in t:
        tt=(x+dx,y+dy,z+dz)
        if tt not in v and all(-10<=j<=40 for j in tt) and b[x+dx][y+dy][z+dz]!=1:
            q.append(tt)
u=0
for i in range(-10,40):
    for j in range(-10,40):
        for k in range(-10,40):
            if b[i][j][k]*b[i][j][k+1]==-1:u+=1
            if b[j][k][i]*b[j][k+1][i]==-1:u+=1
            if b[k][i][j]*b[k+1][i][j]==-1:u+=1
print(u)
