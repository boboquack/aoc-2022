s='''addx 1
noop
addx 2
addx 5
addx 2
noop
noop
noop
addx 5
noop
noop
addx 1
addx 2
addx -5
addx 12
addx 1
addx 4
addx 2
noop
addx -1
addx 4
noop
noop
addx -37
addx 21
addx -13
addx -3
noop
addx 3
addx 2
addx 5
addx -2
addx 7
addx -2
addx 2
addx 11
addx -4
addx 3
noop
addx -18
addx 7
addx 14
addx 2
addx 5
addx -39
addx 1
addx 5
noop
noop
noop
addx 1
addx 4
noop
addx 12
addx 10
addx -17
addx 5
addx -17
addx 14
addx 6
noop
addx 3
addx 7
noop
noop
addx 2
addx 3
noop
addx -40
addx 40
addx -33
addx -2
noop
addx 3
addx 2
addx 5
addx -7
addx 8
noop
addx 6
addx 8
addx -11
addx 8
noop
addx -19
addx 27
noop
addx -2
addx 4
noop
addx -10
addx -27
noop
noop
addx 7
addx 4
addx -3
addx 2
addx 5
addx 2
addx -4
addx -3
addx 10
addx 15
addx -8
addx 2
addx 3
addx -2
addx 5
addx 2
addx 2
addx -39
addx 1
addx 3
addx 3
addx 3
noop
addx 2
addx 1
addx 4
addx -1
addx 2
addx 4
addx 1
noop
noop
addx 2
addx 5
addx 3
noop
noop
addx -27
addx 29
noop
addx 3
noop
noop'''
z='''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''
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
