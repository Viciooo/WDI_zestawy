#1. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
#wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
#większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
#która zwróci długość tego ciągu.

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

def ex1(T):
    N = len(T)
    for c in range(N):
        for r in range(1,N):
            k = 0
            if IfPrime(T[r-1][c]) == True and IfPrime(T[r][c]) == True:
                x = T[r][c] - T[r-1][c] #różnica c arytmetycznego
                while r+k+1<N and T[r+k][c] + x == T[r+k+1][c] and IfPrime(T[r+k+1][c]) == True:
                    k += 1
            if k > 0:
                return k+2
    for r in range(N):
        for c in range(1,N):
            k = 0
            if IfPrime(T[r][c-1]) == True and IfPrime(T[r][c]) == True:
                x = T[r][c] - T[r][c-1] #różnica c arytmetycznego
                while c+k+1<N and T[r][c+k] + x == T[r][c+k+1] and IfPrime(T[r][c+k+1]) == True:
                    k += 1
            if k > 0:
                return k+2
    return False

T = [[3,5,3,0],[1,7,7,1],[3,1,11,3],[2,1,2,3]]
for i in T:
    print(i)
print(ex1(T))