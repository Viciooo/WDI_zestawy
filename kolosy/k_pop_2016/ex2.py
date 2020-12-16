'''2. Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. N z zakresu 4...20.
'''
def start(t):
    steps = []
    n = len(t)
    def rec(t,n,c,r=0,m=0):#m = moves
        nonlocal steps
        if r == n-1 and t[r][c] == False:
            steps.append(m)
            return
        if r >= n or r < 0 or c >= n or c < 0 or t[r][c] == True:
            return
        else:
            rec(t,n,c+1,r+2,m+1) or rec(t,n,c-1,r+2,m+1) or rec(t,n,c+2,r+1,m+1) or rec(t,n,c-2,r+1,m+1)
    for i in range(n):
        rec(t,n,i)
    return min(steps) if steps!=[] else "Row full of figures"

t = [[False,True,True,True],[True,True,False,True],[False,True,True,True],[True,True,True,True]]
for i in t:
    print(i)

print(start(t))