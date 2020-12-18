'''Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero.'''

def start(t,n):
    def rec(t,n,c=-10,r=0,suma=0,res=[]):
        if r == n:
            if suma == 0:
                print(res)
                return True
            return
        else:
            for col in range(n):
                if abs(col-c) > 1:
                    a = rec(t,n,col,r+1,suma+t[r][col],res+[col])
                    if a:
                        return True
    if rec(t,n):
        return True
    return False

from random import randint
n = 4
t = [[1, 0, 1, 1],
    [2, 2, 2, -2],
    [2, 2, -2, 2],
    [-2, 0, 1, -1]] 
for i in t:
    print(i)
print("*********")
print(start(t,n))