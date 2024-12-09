s=INPUT.split()

def f(a):
    if len(a)==1:return {'0':0,'1':1,'2':2,'-':-1,'=':-2}[a]
    return 5*f(a[:-1])+f(a[-1])

print(sum(f(a) for a in s))

#from wolfram alpha, manually convert
#13402...2331_5
#2--1=...=-=1_5


