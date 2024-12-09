s=INPUT

def find(orr,clr,obr,ger,ore,cl,ob,time):
    if time==tmax:return 0
    if (orr,clr,obr,ger,ore,cl,ob,time) in mem:return mem[(orr,clr,obr,ger,ore,cl,ob,time)]
    nore=ore+orr
    ncl=cl+clr
    nob=ob+obr
    nge=ger
    wantore=ore+max(tmax-time-3,0)*orr<max(ore_ore,cl_ore,ob_ore,ge_ore)*max(tmax-time-2,0)
    wantcl=cl+max(tmax-time-4,0)*clr<max(tmax-time-3,0)*ob_cl
    wantob=ob+max(tmax-time-3,0)*obr<max(tmax-time-2,0)*ge_ob
    getge=ob+max(tmax-time-2,0)*obr>=max(tmax-time-1,0)*ge_ob and ore+max(tmax-time-1,0)*orr>=max(tmax-time-1,0)*ge_ore
    best=0
    if not getge:best=find(orr,clr,obr,ger,nore,ncl,nob,time+1)
    if ore>=ore_ore and wantore and not getge:best=max(best,find(orr+1,clr,obr,ger,nore-ore_ore,ncl,nob,time+1))
    if ore>=cl_ore and wantcl and not getge:best=max(best,find(orr,clr+1,obr,ger,nore-cl_ore,ncl,nob,time+1))
    if ore>=ob_ore and cl>=ob_cl and wantob and not getge:best=max(best,find(orr,clr,obr+1,ger,nore-ob_ore,ncl-ob_cl,nob,time+1))
    if ore>=ge_ore and ob>=ge_ob:best=max(best,find(orr,clr,obr,ger+1,nore-ge_ore,ncl,nob-ge_ob,time+1))
    best+=nge
    mem[(orr,clr,obr,ger,ore,cl,ob,time)]=best
    return best

val=0
t=0
tmax=24
for i in s.split('\n'):
    t+=1
    ore_ore,cl_ore,ob_ore,ob_cl,ge_ore,ge_ob=[int(j) for j in i.split() if j.isnumeric()]
    mem={}
    val+=t*find(1,0,0,0,0,0,0,0)
print(val)
val=1
tmax=32
for i in s.split('\n')[:3]:
    ore_ore,cl_ore,ob_ore,ob_cl,ge_ore,ge_ob=[int(j) for j in i.split() if j.isnumeric()]
    mem={}
    val*=find(1,0,0,0,0,0,0,0)
print(val)  

'''
def find(orr,clr,obr,ger,ore,cl,ob,time,noorr,noclr,noobr,noger):
    if time==24:return 0
    if (orr,clr,obr,ger,ore,cl,ob,time,noorr,noclr,noobr,noger) in mem:return mem[(orr,clr,obr,ger,ore,cl,ob,time,noorr,noclr,noobr,noger)]
    nore=ore+orr
    ncl=cl+clr
    nob=ob+obr
    nge=ger
    best=0
    avorr=0 if noorr else ore//ore_ore
    avclr=0 if noclr else ore//cl_ore
    avobr=0 if noobr else min(ore//ob_ore,cl//ob_cl)
    avger=0 if noger else min(ore//ge_ore,ob//ge_ob)
    for iorr in range(avorr+1):
        for iclr in range(avclr+1):
            for iobr in range(avobr+1):
                for iger in range(avger+1):
                    more=ore_ore*iorr+cl_ore*iclr+ob_ore*iobr+ge_ore*iger
                    mcl=ob_cl*iobr
                    mob=ge_ob*iger
                    if more<=ore and mcl<=cl and mob<=ob:
                        best=max(best,find(orr+iorr,clr+iclr,obr+iobr,ger+iger,nore-more,ncl-mcl,nob-mob,time+1,ore-more>=ore_ore,ore-more>=cl_ore,ore-more>=ob_ore and cl-mcl>=ob_cl,ore-more>=ge_ore and ob-mob>=ge_ob)+nge)
    for borr in range(noorr,2):
        for bclr in range(noclr,2):
            for bobr in range(noobr,2):
                for bger in range(noger,2):
                    mem[(orr,clr,obr,ger,ore,cl,ob,time,borr,bclr,bobr,bger)]=best
    return best
'''
