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

#def ex3(t1,t2):
#Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
#sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
#co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
#    N = len(t1)

def ToBinary(n):#zamienia liczbę na binarną 
    l =[]
    while n // 2 != 0:
        l.append(n%2)
        n //=2
    l.append(n%2)
    l = l[::-1]
    tmp = ''
    for i in range(len(l)):
        tmp += str(l[i])
    return int(tmp)

def Count1(n):
    cnt = 0
    while n != 0:
        if n % 10 == 1:
            cnt += 1
        n //= 10
    return cnt

def TwoDimCopy(t): #copy of 2 dimentional list/array idk
    N = len(t)
    tab = [0]*N
    for i in range(N):
        tab[i] = [0]*N
    for r in range(N):
        for c in range(N):
            tab[r][c] = t[r][c]
    return tab

def ex4(t):
#Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
#można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
#posiadał nieparzystą liczbę jedynek.
    N = len(t)
    tab = [0]*N
    for i in range(N):
        tab[i] = [0]*N
    
    for r in range(N):
        for c in range(N):
            if Count1(ToBinary(t[r][c])) % 2 == 0:
                tab[r][c] = 1
    
    for x in range(N):
        for y in range(N):
            for z in range(y+1,N):
                flag = True
                print("x",x,"y",y,"z",z)
                for r in range(N):
                    if r == x:
                        continue
                    for c in range(N):
                        if c == z or c == y:
                            continue
                        Print2DmTab(tab)
                        if tab[r][c] == 1:
                            flag = False
                            break
        if flag == True:
            return True
    return False



def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])

def GenRndTab(length,start,end): #generuje tablicę jednowymiarową
    from random import randint
    tab = []
    for _ in range(length):
        tab.append(randint(start,end))
    return tab
    
if __name__ == "__main__":
    N = 3
    t = [[3,3,3],[2,1,3],[1,3,1]]
    print(ex4(t))
