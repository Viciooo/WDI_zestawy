'''
2. Dana jest tablica int t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica
int w[N]. Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby
suma liczb na polach szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy
przekazać tablice t i w, funkcja powinna zwrócić numery kolumn z których usunięto wieże.'''

def suma(r1,r2,c1,c2,T,N):
    s = 0
    for i in range(N):
        s += T[i][c1] + T[i][c2] + T[r1][i] + T[r2][i] 
    s -= 2*T[r1][c1] +2*T[r2][c2]
    if r1 != r2:
        s -= T[r2][c1] + T[r1][c2]
    return s

def start(t,w,N):
    maxi = -1
    for i in range(N):
        s = t[w[i]][i]
        for j in range(i+1,N):
            print(j)
            if s + t[w[j]][j] > maxi:
                c1, c2, maxi = i, j, s + t[w[j]][j]
    return c1,c2