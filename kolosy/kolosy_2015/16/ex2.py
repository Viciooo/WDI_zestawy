'''2) Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi z zakresu -9 ..9. Proszę napisać funkcję.która
ustawia na szachownicy dwie wieŹe, tak aby suma liczb na szachowanych polach była największa. Do funkcji należy przekazać tablicę, funkcja
powinna zwrócić położenie wież'''
def suma(r,c,T,N):
    suma = 0
    for x in range(N):
        suma += T[r][x] + T[x][c]
    return suma

def programm(T):
    N = len(T)
    m1, m2, i1, i2 = -1, -1, -1, -1
    for i in range(N*N):
        tmp = suma(i//N,i%N,T,N) 
        if tmp > m1:
            m2, i2, i1, m1 = m1, i1, i, tmp
        elif tmp > m2:
            m2, i2 = tmp, i
    return (i1//N,i1%N),(i2//N,i2%N)
