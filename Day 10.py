s=INPUT
#s=z
l=[20,60,100,140,180,220]
d={'noop':1,'addx':2}
c=0
r=1
su=0
for i in s.split('\n'):
    j=i.split()
    c+=d[j[0]]
    if len(l)>0 and l[0]<=c:
        t=l.pop(0)
        su+=r*t
        #print(t,r)
    if j[0]=='addx':
        r+=int(j[1])
        #print(r)
print(su)
c=0
r=1
def p(r,c):
    if abs(1+(c-1)%40-r)<=1:print(end='#')
    else:print(end='.')
    if c%40==0:print()
for i in s.split('\n'):
    j=i.split()
    if j[0]=='addx':
        c+=1
        p(r,c)
    c+=1
    if len(l)>0 and l[0]<=c:
        t=l.pop(0)
        su+=r*t
        #print(t,r)
    if j[0]=='addx':
        r+=int(j[1])
    p(r,c)
        #print(r)
