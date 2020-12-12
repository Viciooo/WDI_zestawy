#1 zazanczam możliwy ruch figury
#-1 pozycję danej figury
#2 oznaczam pole bicia JEŚLI pozycja bicia jest inna niż pozycja ruchu - tak jak w przypadku pionka

def Wieża(tab,r,c): #tablica i tuple z kordami typu (row,column)
    for i in range(len(tab)):
        tab[i][c] = 1
        tab[r][i] = 1
    #end
    tab[r][c] = -1
    return tab

def Pion(tab,r,c): #zakładając że idzie z góry tablicy do dołu
    tab[r][c] = -1
    if r+1 < len(tab):
        tab[r+1][c] = 1
    if r+1 < N:
        if c+1 < N:
            tab[r+1][c+1] = 2
        if c-1 >= 0:
            tab[r+1][c-1] = 2
    #end
    return tab

def Skoczek(tab,r,c):
    if r+2<N and c+1<N:
        tab[r+2][c+1] = 1
    if r+2<N and c-1>0:
        tab[r+2][c-1] = 1
    if r+1<N and c+2<N:
        tab[r+1][c+2] = 1
    if r+1<N and c-2>0:
        tab[r+1][c-2] = 1
    if r-2>0 and c+1<N:
        tab[r-2][c+1] = 1
    if r-2>0 and c-1>0:
        tab[r-2][c-1] = 1
    if r-1>0 and c+2<N:
        tab[r-1][c+2] = 1
    if r-1>0 and c-2>0:
        tab[r-1][c-2] = 1
    tab[r][c] = -1
    return tab

def Goniec(tab,r,c):
    N = len(tab)
    k = 0
    while r+k < N and c+k < N:
        tab[r+k][c+k] = 1
        k += 1
    #end
    k = 0
    while r+k < N and c-k >= 0:
        tab[r+k][c-k] = 1
        k += 1
    #end
    k = 0
    while r-k >= 0 and c-k >= 0:
        tab[r-k][c-k] = 1
        k += 1
    #end
    k = 0
    while r-k >= 0 and c+k <N:
        tab[r-k][c+k] = 1
        k += 1
    #end
    tab[r][c] = -1
    return tab

def Król(tab,r,c):
    if r+1<N:
        tab[r+1][c] = 1
    if r-1>0:
        tab[r-1][c] = 1
    if c+1<N:
        tab[r][c+1] = 1
    if c-1>0:
        tab[r][c-1] = 1
    if r+1<N and c+1<N:
        tab[r+1][c+1] = 1
    if r+1<N and c-1>0:
        tab[r+1][c-1] = 1
    if r-1>0 and c+1<N:
        tab[r-1][c+1] = 1
    if r-1>0 and c-1<N:
        tab[r-1][c-1] = 1
    tab[r][c] = -1
    return tab

def Królówka(tab,r,c):
    Wieża(tab,r,c)
    Goniec(tab,r,c)
    return tab

def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])

if __name__ == "__main__":
    N = 8
    t = [0]*N
    for i in range(N):
        t[i] = [0]*N
    Print2DmTab(Król(t,7,3))

