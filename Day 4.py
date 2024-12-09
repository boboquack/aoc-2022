s=INPUT.split()
t=0
for i in s:
    x,y=i.split(',')
    a,b=x.split('-')
    c,d=y.split('-')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if (a<=c and d<=b) or (c<=a and b<=d):t+=1
print(t)
t=len(s)
for i in s:
    x,y=i.split(',')
    a,b=x.split('-')
    c,d=y.split('-')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if b<c or d<a:t-=1
print(t)
