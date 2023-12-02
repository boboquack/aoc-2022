s='''Monkey 0:
  Starting items: 89, 95, 92, 64, 87, 68
  Operation: new = old * 11
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 1:
  Starting items: 87, 67
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 95, 79, 92, 82, 60
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 3:
  Starting items: 67, 97, 56
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 4:
  Starting items: 80, 68, 87, 94, 61, 59, 50, 68
  Operation: new = old * 7
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 5:
  Starting items: 73, 51, 76, 59
  Operation: new = old + 8
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 6:
  Starting items: 92
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 7:
  Starting items: 99, 76, 78, 76, 79, 90, 89
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 5'''.split('\n\n')
ss='''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''.split('\n\n')
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
