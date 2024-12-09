s=INPUT.split()
l=[[int(i) for i in j] for j in s]
b=[[False]*len(i) for i in l]
for i in range(len(l)):
    m=-1
    for j in range(len(l[i])):
        if l[i][j]>m:
            b[i][j]=True
            m=l[i][j]
    m=-1
    for j in range(len(l[i])-1,-1,-1):
        if l[i][j]>m:
            b[i][j]=True
            m=l[i][j]
for i in range(len(l[0])):
    m=-1
    for j in range(len(l)):
        if l[j][i]>m:
            b[j][i]=True
            m=l[j][i]
    m=-1
    for j in range(len(l)-1,-1,-1):
        if l[j][i]>m:
            b[j][i]=True
            m=l[j][i]
print(sum(sum(i) for i in b))
u=[[-1]*len(i) for i in l]
d=[[-1]*len(i) for i in l]
ll=[[-1]*len(i) for i in l]
r=[[-1]*len(i) for i in l]
for i in range(len(l)):
    stops=[0]*10
    for j in range(len(l[i])):
        ll[i][j]=j-stops[l[i][j]]
        for k in range(l[i][j]+1):
            stops[k]=j
    stops=[len(l[i])-1]*10
    for j in range(len(l[i])-1,-1,-1):
        r[i][j]=stops[l[i][j]]-j
        for k in range(l[i][j]+1):
            stops[k]=j
for i in range(len(l[0])):
    stops=[0]*10
    for j in range(len(l)):
        u[j][i]=j-stops[l[j][i]]
        for k in range(l[j][i]+1):
            stops[k]=j
    stops=[len(l)-1]*10
    for j in range(len(l)-1,-1,-1):
        d[j][i]=stops[l[j][i]]-j
        for k in range(l[j][i]+1):
            stops[k]=j
print(max(max(ll[i][j]*u[i][j]*d[i][j]*r[i][j] for i in range(len(l))) for j in range(len(l[0]))))
