s=INPUT.split('\n')
l=[['.']*1000 for i in range(2000)]
my=0
for i in s:
    for j,k in zip(i.split(' -> '),i.split(' -> ')[1:]):
        a,b=j.split(',')
        a=int(a)
        b=int(b)
        c,d=k.split(',')
        c=int(c)
        d=int(d)
        if a==c:
            for i in range(min(b,d),max(b,d)+1):
                l[a][i]='#'
        else:
            for i in range(min(a,c),max(a,c)+1):
                l[i][b]='#'
        my=max(b,d,my)
t=0
while True:
    x=500
    y=0
    while y<999 and (l[x][y+1]=='.' or l[x-1][y+1]=='.' or l[x+1][y+1]=='.'):
        y+=1
        if l[x][y]!='.':x-=1
        if l[x][y]!='.':x+=2
    if y==999:break
    l[x][y]='o'
    t+=1
print(t)
for i in range(2000):
    l[i][my+2]='#'
while l[500][0]!='o':
    x=500
    y=0
    while l[x][y+1]=='.' or l[x-1][y+1]=='.' or l[x+1][y+1]=='.':
        y+=1
        if l[x][y]!='.':x-=1
        if l[x][y]!='.':x+=2
    l[x][y]='o'
    t+=1
print(t)
