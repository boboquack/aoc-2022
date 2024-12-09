s=INPUT1

t=INPUT2
l=[[] for i in range(9)]
for i in s.split('\n')[::-1]:
    for j in range(9):
        if i[j*4+1]!=' ':
            l[j].append(i[j*4+1])
for i in t.split('\n'):
    a,b,c,d,e,f=i.split()
    b,d,f=int(b),int(d),int(f)
    for i in range(b):
        l[f-1].append(l[d-1].pop())
print(''.join(i[-1] for i in l))
l=[[] for i in range(9)]
for i in s.split('\n')[::-1]:
    for j in range(9):
        if i[j*4+1]!=' ':
            l[j].append(i[j*4+1])
for i in t.split('\n'):
    a,b,c,d,e,f=i.split()
    b,d,f=int(b),int(d),int(f)
    z=l[d-1][-b:]
    l[d-1]=l[d-1][:-b]
    l[f-1]=l[f-1]+z
print(''.join(i[-1] for i in l))
