s=INPUT.split()

ss=SAMPLE1.split()

ss=SAMPLE2.split()

e=[]
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j]=='#':e.append((i,j))
def m(r,c,se,v):
    if all(t not in se for t in [(r-1,c-1),(r,c-1),(r+1,c-1),(r-1,c),(r+1,c),(r-1,c+1),(r,c+1),(r+1,c+1)]):
        return None
    if v%4<=0 and all(t not in se for t in [(r-1,c-1),(r-1,c),(r-1,c+1)]):
        return (r-1,c)
    if v%4<=1 and all(t not in se for t in [(r+1,c-1),(r+1,c),(r+1,c+1)]):
        return (r+1,c)
    if v%4<=2 and all(t not in se for t in [(r-1,c-1),(r,c-1),(r+1,c-1)]):
        return (r,c-1)
    if all(t not in se for t in [(r-1,c+1),(r,c+1),(r+1,c+1)]):
        return (r,c+1)
    if all(t not in se for t in [(r-1,c-1),(r-1,c),(r-1,c+1)]):
        return (r-1,c)
    if all(t not in se for t in [(r+1,c-1),(r+1,c),(r+1,c+1)]):
        return (r+1,c)
    if all(t not in se for t in [(r-1,c-1),(r,c-1),(r+1,c-1)]):
        return (r,c-1)
    return None
def loop():
    global e,v
    se=set(e)
    prop=[m(r,c,se,v) for r,c in e]
    if all(i==None for i in prop):return False
    un=set()
    bad=set()
    for i in prop:
        if i in un:
            bad.add(i)
        else:
            un.add(i)
    ne=[0]*len(e)
    for i in range(len(e)):
        if prop[i]==None or prop[i] in bad:ne[i]=e[i]
        else:ne[i]=prop[i]
    e=ne
    v+=1
    return True
v=0
for i in range(10):loop()
a=max(t[0] for t in e)
b=min(t[0] for t in e)
c=max(t[1] for t in e)
d=min(t[1] for t in e)
print((a-b+1)*(c-d+1)-len(e))

while loop():pass
print(v+1)
