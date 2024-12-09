s=INPUT.split('\n')
d={}
for i in s:
 a,b=i.split(': ')
 if b.isnumeric():d[a]=int(b)
 else:d[a]=(b[:4],b[5],b[-4:])
def f(v):
 if type(d[v])==int:return d[v]
 x,y,z=d[v]
 return eval(str(f(x))+y+str(f(z)))
print(f('root'))

a,b,c=d['root']
u=f(c)
hi=10**15
lo=1
while lo<hi:
 m=(lo+hi)//2
 d['humn']=m
 v=f(a)
 if v==u:
  print(m)
  break
 if v<u:hi=m-1
 else:lo=m+1
else: print(lo) #float issues prob

#alternatively

d={}
for i in s:
 a,b=i.split(': ')
 if b.isnumeric():d[a]=int(b)
 else:d[a]=(b[:4],b[5],b[-4:])
def f(v):
 if type(d[v])==int or type(d[v])==type(1j):return d[v]
 x,y,z=d[v]
 return eval(str(f(x))+y+str(f(z)))
print(int((f('root')+.5)//1))

a,b,c=d['root']
d['humn']=1j
print(int(((-f(a).real+f(c))/f(a).imag+.5)//1))
