s=INPUT.split('\n\n')

def comp(x,y):
    if type(x)==type(y)==int:
        if x<y:return 1
        if x>y:return -1
        return 0
    if type(x)==int:return comp([x],y)
    if type(y)==int:return comp(x,[y])
    for i in range(min(len(x),len(y))):
        a=comp(x[i],y[i])
        if a!=0:return a
    if len(x)<len(y):return 1
    if len(x)>len(y):return -1
    return 0

assert all(all(i in '[]1234567890,\n' for i in t) for t in s)
t=0
for i in range(len(s)):
    a,b=s[i].split()
    a=eval(a)
    b=eval(b)
    if comp(a,b)==1:t+=i+1
print(t)
sz=SAMPLE.split('\n\n')
s=[eval(i.split()[0]) for i in s]+[eval(i.split()[1]) for i in s]+[[[2]]]+[[[6]]]
for i in range(len(s)):
    for j in range(len(s)-1):
        if comp(s[j],s[j+1])<0:
            v=s[j+1]
            s[j+1]=s[j]
            s[j]=v
print((s.index([[2]])+1)*(s.index([[6]])+1))
