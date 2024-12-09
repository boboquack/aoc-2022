s=INPUT
ss=SAMPLE
s=[list(i[1:-1]) for i in s.split()[1:-1]]

dirs={'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1),'.':(0,0)}
bl=set()
rows=len(s)
cols=len(s[0])
for i in range(rows):
    for j in range(cols):
        if s[i][j]!='.':bl.add((s[i][j],i,j))

def f(t):
    t,r,c=t
    dr,dc=dirs[t]
    return (t,(r+dr)%rows,(c+dc)%cols)

bl=set()
for i in range(rows):
    for j in range(cols):
        if s[i][j]!='.':bl.add((s[i][j],i,j))

mov={(-1,0,0)}
turns=0
p1=False
while (rows,cols-1,2) not in mov:
    turns+=1
    bl={f(i) for i in bl}
    nmov=set()
    for r,c,g in mov:
        for dr,dc in dirs.values():
            if ((0<=r+dr<rows and 0<=c+dc<cols) or (r+dr,c+dc)==(-1,0) or (r+dr,c+dc)==(rows,cols-1)) and not any((t,r+dr,c+dc) in bl for t in '<>v^'):
                ng=g
                if (r+dr,c+dc)==(rows,cols-1) and g==0:ng=1
                if (r+dr,c+dc)==(-1,0) and g==1:ng=2
                nmov.add((r+dr,c+dc,ng))
    mov=nmov
    if not p1 and (rows,cols-1,1) in mov:
        print(turns)
        p1=True

