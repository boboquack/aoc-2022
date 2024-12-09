s=INPUT
l=[i.split() for i in s.split('\n')]
def sc(a,b):
    if a=='A':
        if b=='X':
            return 4
        if b=='Y':
            return 8
        if b=='Z':
            return 3
    if a=='B':
        if b=='X':
            return 1
        if b=='Y':
            return 5
        if b=='Z':
            return 9
    if a=='C':
        if b=='X':
            return 7
        if b=='Y':
            return 2
        if b=='Z':
            return 6

print(sum(sc(a,b) for a,b in l))

def sc(a,b):
    if a=='A':
        if b=='X':
            return 3
        if b=='Y':
            return 4
        if b=='Z':
            return 8
    if a=='B':
        if b=='X':
            return 1
        if b=='Y':
            return 5
        if b=='Z':
            return 9
    if a=='C':
        if b=='X':
            return 2
        if b=='Y':
            return 6
        if b=='Z':
            return 7

print(sum(sc(a,b) for a,b in l))
