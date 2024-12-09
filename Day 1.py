s=INPUT
l=s.split('\n\n')
t=[[int(i) for i in j.split()] for j in l]
u=[sum(i) for i in t]
print(max(u))
u.sort()
print(sum(u[-3:]))

