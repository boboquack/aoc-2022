import time
x=time.time()
s='''Valve XG has flow rate=0; tunnels lead to valves CR, OH
Valve ZF has flow rate=7; tunnels lead to valves SC, BY, PM, LW, CJ
Valve RD has flow rate=13; tunnels lead to valves JS, VM
Valve XJ has flow rate=0; tunnels lead to valves JO, YO
Valve CJ has flow rate=0; tunnels lead to valves UA, ZF
Valve UA has flow rate=0; tunnels lead to valves ZP, CJ
Valve EQ has flow rate=0; tunnels lead to valves ZP, RP
Valve IU has flow rate=0; tunnels lead to valves EV, CN
Valve QM has flow rate=0; tunnels lead to valves XA, CN
Valve WC has flow rate=0; tunnels lead to valves JS, OH
Valve MU has flow rate=0; tunnels lead to valves AA, ZP
Valve MW has flow rate=11; tunnels lead to valves BM, AG, RG, NL
Valve XA has flow rate=0; tunnels lead to valves JO, QM
Valve OH has flow rate=12; tunnels lead to valves WC, YS, XG, KO
Valve QD has flow rate=20; tunnels lead to valves BY, KY, CR, RP
Valve OE has flow rate=0; tunnels lead to valves FB, BU
Valve CB has flow rate=0; tunnels lead to valves AA, FX
Valve TB has flow rate=23; tunnel leads to valve VM
Valve PM has flow rate=0; tunnels lead to valves ZF, AA
Valve YS has flow rate=0; tunnels lead to valves OH, RG
Valve KO has flow rate=0; tunnels lead to valves OH, VT
Valve AA has flow rate=0; tunnels lead to valves PM, MU, BM, AW, CB
Valve RG has flow rate=0; tunnels lead to valves YS, MW
Valve BU has flow rate=0; tunnels lead to valves OE, EV
Valve RK has flow rate=0; tunnels lead to valves KY, FX
Valve JO has flow rate=18; tunnels lead to valves NL, SX, XA, XJ
Valve AG has flow rate=0; tunnels lead to valves IS, MW
Valve AW has flow rate=0; tunnels lead to valves BS, AA
Valve ZP has flow rate=9; tunnels lead to valves UA, NG, DU, MU, EQ
Valve KY has flow rate=0; tunnels lead to valves QD, RK
Valve EV has flow rate=19; tunnels lead to valves VT, BU, IU, SX
Valve FB has flow rate=24; tunnel leads to valve OE
Valve DU has flow rate=0; tunnels lead to valves IS, ZP
Valve NG has flow rate=0; tunnels lead to valves FX, ZP
Valve HC has flow rate=0; tunnels lead to valves CN, HB
Valve SC has flow rate=0; tunnels lead to valves IS, ZF
Valve HB has flow rate=22; tunnel leads to valve HC
Valve VM has flow rate=0; tunnels lead to valves RD, TB
Valve LW has flow rate=0; tunnels lead to valves ZF, FX
Valve SX has flow rate=0; tunnels lead to valves EV, JO
Valve FX has flow rate=6; tunnels lead to valves FA, NG, RK, LW, CB
Valve JS has flow rate=0; tunnels lead to valves WC, RD
Valve BM has flow rate=0; tunnels lead to valves MW, AA
Valve FA has flow rate=0; tunnels lead to valves IS, FX
Valve RP has flow rate=0; tunnels lead to valves QD, EQ
Valve NL has flow rate=0; tunnels lead to valves MW, JO
Valve CN has flow rate=15; tunnels lead to valves HC, QM, IU
Valve BS has flow rate=0; tunnels lead to valves IS, AW
Valve KP has flow rate=25; tunnel leads to valve YO
Valve YO has flow rate=0; tunnels lead to valves XJ, KP
Valve CR has flow rate=0; tunnels lead to valves XG, QD
Valve BY has flow rate=0; tunnels lead to valves QD, ZF
Valve IS has flow rate=5; tunnels lead to valves DU, SC, AG, FA, BS
Valve VT has flow rate=0; tunnels lead to valves KO, EV'''

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
print(time.time()-x)
x=time.time()
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
print(time.time()-x)

ss='''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

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
