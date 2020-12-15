'''Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero.
'''

def rek(T, N, w=0, k=0, suma=0):
    if w == N:
        return suma == 0
    for i in range(N):
        if abs(k-i) > 1 and rek(T, N, w+1, i, suma+T[w][i]):
            return True
    return False