def can_move(t,r,c):
    if r < len(t) and r >= 0 and c < len(t) and c >= 0:
        if t[r][c] == False:
            return True

def jump(t,i,j):
    t[i][j] = True
    ruchy = (2,1),(1,2),(-2,1),(-2,-1),(2,-1),(-1,-2),(1,-2),(-1,2)
    for elem in ruchy:
        if can_move(t,i+elem[0],j+elem[1]):
            if jump(t,i+elem[0],j+elem[1]):
                return True

    for k in t:
        for g in k:
            if g == False:
                t[i][j] = False
                return False
    t[i][j] = False
    return True

def start(dim):
    for i in range((dim+1)//2):
        for j in range(i,(dim+1)//2):
            if jump([[False for _ in range(dim)]for _ in range(dim)],i,j):
                return True
    return False

print(start(7))