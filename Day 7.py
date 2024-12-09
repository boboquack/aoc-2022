s=INPUT.split('\n')
class di:
    def __init__(self,name,up):
        self.files=[]
        self.subs=[]
        self.name=name
        self.up=up
        self.listed=False
        self.sizeval=-1
    def size(self):
        if self.sizeval!=-1:return self.sizeval
        else:
            t=0
            for i in self.files:t+=int(i[0])
            for i in self.subs:t+=i.size()
            self.sizeval=t
            return t
head=di('/',None)
dirs=[head]
now=head
for i in s:
    if i[0]=='$':
        listing=None
        if i[2]=='c':
            if i[5]=='.':
                now=now.up
            else:
                for fol in now.subs:
                    if fol.name==i[5:]:
                        now=fol
        else:
            if not now.listed:
                now.listed=True
                listing=now
    elif listing!=None:
        t=i.split()
        if t[0]=='dir':
            new=di(t[1],now)
            now.subs.append(new)
            dirs.append(new)
        else:
            now.files.append(t)
t=0
for i in dirs:
    if i.size()<100000:t+=i.size()
print(t)
t=100000000
for i in dirs:
    if head.size()-i.size()<=40000000 and i.size()<t:
        t=i.size()
print(t)
