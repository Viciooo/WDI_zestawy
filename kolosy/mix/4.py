'''Zadanie 1.
Tablica t[N][N] jest wypełniona liczbami naturalnymi. W dokładnie jednym wierszu istnieje dokładnie jeden fragment ciągu Fibonacciego o długości
większej niż 2, mniejszej niż N. Napisz funkcję, która znajdzie ten fragment i
zwróci numer wiersza, w którym się znajduje.
'''
def GenFibNums(n):
    a = b = 1
    while b < n:
        a, b = b, a+b
    return (a,b) if b == n else (0,0)

def ex(t):
    n = len(t)
    for r in range(n):
        c = 0
        while c< n-2:
            a, b = GenFibNums(t[r][c])
            if b != 0:
                k = 1
                while t[r][c+k] == a+b:
                    a, b = b, a+b
                    k += 1
                    if k > 2:
                        print("Działa : DDDD")
                        return r
            c += 1
    return "nie dziala :("

tab = [[1 for _ in range(7)] for _ in range(7)]
tab[3] = [1, 1, 2, 3, 5, 8, 1]

for i in tab:
    print(i)

print(ex(tab))

