s=[int(i) for i in INPUT.split()]
#s=[1, 2, -3, 3, -2, 0, 4]
l=[s[i]*8192+i for i in range(len(s))]
x=len(l)
for i in range(len(s)):
    r=l.index(s[i]*8192+i)
    l=l[r+1:]+l[:r]
    v=s[i]%(x-1)
    l=l[:v]+[s[i]*8192+i]+l[v:]
u=l.index(0+s.index(0))
print(l[(u+1000)%len(l)]//8192+l[(u+2000)%len(l)]//8192+l[(u+3000)%len(l)]//8192)

s=[i*811589153 for i in s]
l=[s[i]*8192+i for i in range(len(s))]
for t in range(10):
    for i in range(len(s)):
        r=l.index(s[i]*8192+i)
        l=l[r+1:]+l[:r]
        v=s[i]%(x-1)
        l=l[:v]+[s[i]*8192+i]+l[v:]
u=l.index(0+s.index(0))
print(l[(u+1000)%len(l)]//8192+l[(u+2000)%len(l)]//8192+l[(u+3000)%len(l)]//8192)
   
