'''Zadanie 2.1a (2017/2018)
Dana jest tablica t[N][N] reprezentująca szachownicę, wypełniona liczbami naturalnymi. na
szachownicy znajdują się dwie wieże. Proszę napisać funkcję, która odpowiada na pytanie: czy
istnieje ruch wieży zwiększający sumę liczb na “szachowanych” przez wieże polach? Do funkcji
należy przekazać tablicę oraz położenia dwóch wież, funkcja powinna zwrócić wartość logiczną.
Uwagi: zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola, na którym stoi.
N to globalny const int.'''
global n
def suma_r(r,t):
    s = 0
    for c in range(n):
        s += t[r][c]
    return s

def suma_c(c,t):
    s = 0
    for r in range(n):
        s += t[r][c]
    return s

def ruchy(y1,x1,y2,x2):
    if x1 != x2:
        return range(n)
    if y1 < y2:
        return range(y2)
    else:
        return range(y2+1,n)

def func(t,r1,c1,r2,c2):

    sumOfR = [0]*n
    sumOfC = [0]*n

    for i in range(n):
        sumOfR[i] += suma_r(i,t)
        sumOfC[i] += suma_c(i,t)

    def zlicz(r1,c1,r2,c2):
        suma = sumOfR[r1] + sumOfR[r2] + sumOfC[c1] + sumOfC[c2] 
        suma -= 2*(t[r1][c1] + t[r2][c2])
        if r1 == r2:
            suma = suma - sumOfR[r1]
        elif c1 == c2:
            suma = suma - sumOfC[c1]
        else:
            suma -= (t[r1][c2] + t[r2][c1])
        return suma

    s = zlicz(r1,c1,r2,c2)
    
    for row1 in ruchy(r1,c1,r2,c2):
        if zlicz(row1,c1,r2,c2) > s:
            return True

    for col1 in ruchy(c1,r1,c2,r2):
        if zlicz(r1,col1,r2,c2) > s:
            return True

    for row2 in ruchy(r2,c2,r1,c1):
        if zlicz(row2,c2,r1,c1) > s:
            return True

    for col2 in ruchy(c2,r2,c1,r1):
        if zlicz(r2,col2,r1,c1) > s:
            return True

    return False

t1=[[0,0,0,100],[0,100,0,0],[0,0,0,0],[0,0,0,0]]
n = 3
from random import randint
#t = [[randint(1,5) for _ in range(n)] for _ in range(n)]
for i in t1:
    print(i)

print(func(t1,0,1,2,1))

