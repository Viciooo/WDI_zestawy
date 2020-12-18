'''Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool.'''

def IfPrime(n): #sprawdza czy pierwsza
    if n <=1:
        return False
    if n ==2 or n ==3:
        return True
    if n %2==0 or n%3==0:
        return False
    i = 6
    while (i-1)**2<=n:
        if n %(i-1) == 0:
            return False
        if n%(i+1) == 0:
            return False
        i+=6
    return True

def func(tab,N):
    for i in range(N*N):
        r = i // N
        c = i % N
        if r+2<N and c+1<N:
            if IfPrime(tab[r+2][c+1] + tab[r][c]):
                return True
        if r+2<N and c-1>0:
            if IfPrime(tab[r+2][c-1] + tab[r][c]):
                return True
        if r+1<N and c+2<N:
            if IfPrime(tab[r+1][c+2] + tab[r][c]):
                return True
        if r+1<N and c-2>0:
            if IfPrime(tab[r+1][c-2] + tab[r][c]):
                return True
        if r-2>0 and c+1<N:
            if IfPrime(tab[r-2][c+1] + tab[r][c]):
                return True
        if r-2>0 and c-1>0:
            if IfPrime(tab[r-2][c-1] + tab[r][c]):
                return True
        if r-1>0 and c+2<N:
            if IfPrime(tab[r-1][c+2] + tab[r][c]):
                return True
        if r-1>0 and c-2>0:
            if IfPrime(tab[r-1][c-2] + tab[r][c]):
                return True
    return False

T = [[0,4,0,0],[0,0,0,0],[0,0,4,0],[0,0,0,0]]

for i in T:
    print(i)

print(func(T,4))