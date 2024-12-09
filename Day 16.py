s=INPUT

d={}
f={}
for i in s.split('\n'):
    valve=i[6:8]
    flow=int(i[23:].split(';')[0])
    links=i.split('to valve')[1].split(', ')
    links[0]=links[0].split(' ')[1]
    d[valve]=links
    f[valve]=flow

dist={i:{j:0 if i==j else float('inf') for j in d} for i in d}
for i in d:
    for j in d[i]:
        dist[i][j]=1
for k in d:
    for i in d:
        for j in d:
            if dist[i][j]+dist[j][k]<dist[i][k]:
                dist[i][k]=dist[i][j]+dist[j][k]

mem={}
pos=sorted([i for i in d if f[i]])
w=lambda i:True
glob=30
def fun(loc, op, tim, yes):
    if tim>=glob+1:return 0
    v=0
    for i in pos:
        v*=2
        if i not in op and w(i):v+=1
    if (loc,v,glob-tim,yes) in mem:return mem[(loc,v,glob-tim,yes)]
    if yes:
        op.add(loc)
        m=(glob-tim)*f[loc]+fun(loc,op,tim+1,False)
        op.remove(loc)
    else:
        m=0
        for i in d:
            if f[i] and i not in op and w(i):
                m=max(m,fun(i,op,tim+dist[loc][i],True))
    mem[(loc,v,glob-tim,yes)]=m
    return m

print(fun('AA',set(),1,False))

import itertools
allowed=[i for i in d if f[i]]
give={}
glob=26
w=lambda i:i in n
for r in range(len(allowed)+1):
    for n in itertools.combinations(allowed,r):
        give[n]=fun('AA',set(),1,False)
m=0
for i in give:
    j=tuple(k for k in allowed if k not in i)
    m=max(m,give[i]+give[j])
print(m)

ss=sample

'''
def fun(loc,op,tot,tim):
    if tim==31:return tot
    if loc not in op:
        op.add(loc)
        m=tot+f[loc]*(30-tim)+fun(loc,op,tot,tim+1)
        op.remove(loc)
    else:m=tot
    for i in d[loc]:
        m=max(m,fun(i,op,tot,tim+1))
    return m

print(fun('AA',set(),0,1))
'''

'''
mem={}
pos=sorted([i for i in d if f[i]])
def fun(loc,loc2, op, tim, prog,prog2):
    if tim>=27:return 0
    v=0
    for i in pos:
        v*=2
        if i in op:v+=1
    if (loc,loc2,v,tim,prog,prog2) in mem:return mem[(loc,loc2,v,tim,prog,prog2)]
    m=0
    if prog==0:
        op.add(loc)
        m=(27-tim)*f[loc]
    if prog2==0 and (prog!=0 or loc!=loc2):
        op.add(loc2)
        m+=(27-tim)*f[loc2]
    if prog>0:new={loc:prog-1}
    else:
        new={i:dist[loc][i] for i in d if f[i] and i not in op}
        new[loc2]=-1
    if prog2>0:new2={loc2:prog2-1}
    else:
        new2={i:dist[loc2][i] for i in d if f[i] and i not in op}
        new2[loc2]=-1
    mm=0
    if loc==loc2=='AA':print(len(new)*len(new2))
    t=0
    for j in new:
        for j2 in new2:
            t+=1
            if loc==loc2=='AA':print(t)
            if j2!=j:
                mm=max(mm,fun(j,j2,op,tim+1,new[j],new2[j2]))
    if prog==0:
        op.remove(loc)
    if prog2==0 and (prog!=0 or loc!=loc2):
        op.remove(loc2)
    mem[(loc,loc2,v,tim,prog,prog2)]=m+mm
    #if m+mm==1626:print(loc,loc2,bin(v),tim,prog,prog2,m,mm,sep='\t')
    #if m+mm==1166:print(loc,loc2,bin(v),tim,prog,prog2,m,mm,sep='\t')
    #if m+mm==704:print(loc,loc2,bin(v),tim,prog,prog2,m,mm,sep='\t')
    return m+mm
print(fun('AA','AA',set(),1,-1,-1))
'''
