s=INPUT.split()
for j in range(len(s)):
    i=s[j]
    if 'S' in i:
        sr,sc=j,i.index('S')
        i=i[:sc]+'a'+i[sc+1:]
    if 'E' in i:
        er,ec=j,i.index('E')
        i=i[:ec]+'z'+i[ec+1:]
    s[j]=i
visited=set()
tovisit=[(sr,sc,0)]
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
while tovisit:
    r,c,d=tovisit.pop(0)
    if (r,c) in visited: continue
    visited.add((r,c))
    if (r,c)==(er,ec):
        print(d)
        break
    for dr,dc in dirs:
        if 0<=dr+r<len(s) and 0<=dc+c<len(s[0]) and ord(s[r+dr][c+dc])-ord(s[r][c])<=1:
            tovisit.append((r+dr,c+dc,d+1))
tovisit=[]
for j in range(len(s)):
    for i in range(len(s[0])):
        if s[j][i]=='a':tovisit.append((j,i,0))
visited=set()
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
while tovisit:
    r,c,d=tovisit.pop(0)
    if (r,c) in visited: continue
    visited.add((r,c))
    if (r,c)==(er,ec):
        print(d)
        break
    for dr,dc in dirs:
        if 0<=dr+r<len(s) and 0<=dc+c<len(s[0]) and ord(s[r+dr][c+dc])-ord(s[r][c])<=1:
            tovisit.append((r+dr,c+dc,d+1))
