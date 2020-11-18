def GenRnd2DmArr(N,start,end): #generuje dwuwymiarowe tablice
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

def ex1():
#Prosze napisac w jezyku Python program, który wyznacza ostatnia niezerowa cyfra N! Program powinien
#działac dla N rzedu 3000.
    N = 3000
    x = 0
    y = 1
    while N != 1:
        if N % 5 ==0:
            N //= 5
            x += N
            print(x)
        else:
            y *= N%10
            N -= 1
            print(y)
    if x % 4 == 0:
        x = 0
    print(((2**x)*y)%10)

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

def ex2(t):
#1. Dane są deklaracje reprezentujące szachownicę o boku długości N:
#const int N= …
#int tab[N][N];
#Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
#klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
#szachownicy, że:
#- oba klocki są prostopadle do siebie,
#- w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
#- największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.
    #pion = [0][0] #druga część domina to [1,0]
    #poz = [0][0] #druga część domina to [0,1]
    for r1 in range(N-1):
        for c1 in range(N):
            for r2 in range(N):
                for c2 in range(N-1):
                    if r2 == r1 or r2 == r1+1 or c1 == c2 or c1 == c2+1:
                        continue
                    a = t[r1][c1]
                    b = t[r1+1][c1]
                    c = t[r2][c2]
                    d = t[r2][c2+1]
                    if a == b or a == c or a == d or b == c or b == d or c == d:
                        continue
                    if IfPrime(a) == True and IfPrime(b) == True and IfPrime(c) == True and IfPrime(d) == True:              
                        print(t[r1][c1],"|",t[r1+1][c1],"&",t[r2][c2],"|",t[r2][c2+1],sep="")

def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])

if __name__ == "__main__":
    N = 5
    t = GenRnd2DmArr(N,1,100)
    Print2DmTab(t)
    ex2(t)
