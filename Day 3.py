s=INPUT.split()
t=0
for i in s:
    m=i[:len(i)//2]
    n=i[len(i)//2:]
    v=list(set(m)&set(n))[0]
    if ord(v)>96:t+=ord(v)-96
    else:t+=ord(v)-64+26
print(t)
t=0
for i in range(len(s)//3):
    q=s[i*3]
    r=s[i*3+1]
    u=s[i*3+2]
    v=list(set(q)&set(r)&set(u))[0]
    if ord(v)>96:t+=ord(v)-96
    else:t+=ord(v)-64+26
print(t)
