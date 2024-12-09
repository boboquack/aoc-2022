s=INPUT.split('\n\n')
m=[]
op=[]
val=[]
div=[]
tr=[]
fa=[]
for i in s:
    a,b,c,d,e,f=i.split('\n')
    b=[int(i) for i in b.split(': ')[1].split(', ')]
    m.append(b)
    op.append(c.split('old ')[1][0])
    if c.split('old ')[1].split(' ')[1]=='old':
        val.append(None)
    else:
        val.append(int(c.split('old ')[1].split(' ')[1]))
    div.append(int(d.split('by ')[1]))
    tr.append(int(e.split('monkey ')[1]))
    fa.append(int(f.split('monkey ')[1]))
tot=[0]*len(m)
for i in range(20):
    for j in range(len(m)):
        x=m[j]
        m[j]=[]
        for k in x:
            if val[j]==None:
                k=eval(str(k)+op[j]+str(k))
            else:
                k=eval(str(k)+op[j]+str(val[j]))
            k//=3
            if k%div[j]==0:
                m[tr[j]].append(k)
            else:
                m[fa[j]].append(k)
            tot[j]+=1
tot.sort()
print(tot[-1]*tot[-2])
m=[]
op=[]
val=[]
div=[]
tr=[]
fa=[]
mod=1
for i in s:
    a,b,c,d,e,f=i.split('\n')
    b=[int(i) for i in b.split(': ')[1].split(', ')]
    m.append(b)
    op.append(c.split('old ')[1][0])
    if c.split('old ')[1].split(' ')[1]=='old':
        val.append(None)
    else:
        val.append(int(c.split('old ')[1].split(' ')[1]))
    div.append(int(d.split('by ')[1]))
    mod*=div[-1]
    tr.append(int(e.split('monkey ')[1]))
    fa.append(int(f.split('monkey ')[1]))
tot=[0]*len(m)
for i in range(10000):
    for j in range(len(m)):
        x=m[j]
        m[j]=[]
        for k in x:
            if val[j]==None:
                k=eval(str(k)+op[j]+str(k))
            else:
                k=eval(str(k)+op[j]+str(val[j]))
            k%=mod
            if k%div[j]==0:
                m[tr[j]].append(k)
            else:
                m[fa[j]].append(k)
            tot[j]+=1
tot.sort()
print(tot[-1]*tot[-2])
