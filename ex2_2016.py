'''2. Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
funkcja powinna zwrócić położenie wież.'''

def zad(t,N):
    m1,i1,m2,i2 = -1,-1,-1,-1
    for i in range(N*N):
        #sprawdzamy kolumny
        r = i//N
        c = i%N
        suma = 0
        for col in range(N):
            suma += T[r][col]
        for row in range(N):
            suma += T[row][c]
        suma -= 2*t[r][c]
        if suma > m1:
            m2, m1, i2, i1= m1, suma, i1, i
        elif suma > m2:
            m2, i2 = suma, i
    return (i1//N,i1%N),(i2//N,i2%N)

#17min ze sprawdzeniem zadania

