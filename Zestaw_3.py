def ex1(N):
#Zadanie 1. Dana jest tablica T[N][N]. Prosze napisac funkcje wypełniajaca tablice kolejnymi liczbami
#naturalnymi po spirali.
    #N = 5 #ilość el
    k = 2 #wartość od której startujemy
    t = N*[0]
    for i in range(N):  #t[row][column]
        t[i] = N*[0]
    t[0][0] = 1

    r = 0 #row index
    c = 0 #column index

    while k  <= N*N:

        while c+1< N and t[r][c+1] == 0: # w prawo
            c += 1
            t[r][c] = k
            k += 1

        while r+1 < N and t[r+1][c] == 0: # w dół
            r += 1
            t[r][c] = k
            k += 1

        while c-1 >= 0 and t[r][c-1] == 0: # w lewo
            c -= 1
            t[r][c] = k
            k += 1

        while r-1 >= 0 and t[r-1][c] == 0: #do góry
            r -= 1
            t[r][c] = k
            k += 1

    
    return t
    #for i in range(len(t)):
    #   print(t[i])

def GenRnd2DmArr(N,start,end):
    from random import randint

    t = N*[0]
    c = 0
    r = 0

    for i in range(N):
        t[i] = N*[0]

    while t[N-1][N-1] == 0:
        if c==N:
            r += 1
            c = 0
        t[r][c] = randint(start,end)
        c += 1
    
    return t

def IfMadeOfOddDigits(tab):
    for i in range(len(tab)):
        while tab[i] % 10 != 0:
            tmp = tab[i] % 10
            if tmp % 2 == 0:
                break
            tab[i] //= 10
            if tab[i] == 0:
                return 1
    return 0


def ex2(t):
#Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
#odpowiada na pytanie, czy w kazdym wierszu tablicy wystepuje co najmniej jedna liczba złozona wyłacznie
#z nieparzystych cyfr.

    N = len(t)
    cnt = 0
    for i in range(len(t)):
       print(t[i])   
    for i in range(len(t)):
        cnt += IfMadeOfOddDigits(t[i])   
    if cnt == N:
        return True
    return False
if __name__ == "__main__":
    t = ex1(3)
    print(ex2(t))
