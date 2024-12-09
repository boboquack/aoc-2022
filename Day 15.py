s=INPUT

ss=SAMPLE
z=2000000
zz=10
t=set()
u=set()
for i in s.split('\n'):
    a,b,c=i.split(' at x=')
    sx=int(b.split(', y=')[0])
    sy=int(b.split(', y=')[1].split(': ')[0])
    bx=int(c.split(', y=')[0])
    by=int(c.split(', y=')[1])
    q=abs(bx-sx)+abs(by-sy)
    if abs(sy-z)<=q:
        v=q-abs(sy-z)
        t|=set(range(sx-v,sx+v+1))
    if by==z:u.add(bx)
print(len(t-u))
for i in s.split('\n'):
    a,b,c=i.split(' at x=')
    sx=int(b.split(', y=')[0])
    sy=int(b.split(', y=')[1].split(': ')[0])
    bx=int(c.split(', y=')[0])
    by=int(c.split(', y=')[1])
    q=abs(bx-sx)+abs(by-sy)
    print('\\left|x-'+str(sx)+'\\right|+\\left|y-'+str(sy)+'\\right|\\le'+str(q))
