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
    N = len(t)
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


def PrimeDivList(n): #zwraca listę podzielników pierwszych w postaci tablicy
    l = []
    for i in range(2,n+1):
        if n % i == 0:
            l.append(i)
        while n % i == 0:
            n //= i
    return l

def ex3(t1,t2):
#Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
#sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
#co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
    N = len(t1)
    for x in range(1,N): #długość wycinków
        for s1 in range(N-1): #s - start - 1st index wycinka
            if s1+x >= N:
                break
            suma1 = 0
            cnt = 0
            for i in range(s1,s1+x):
                suma1 += t1[i]
                cnt += 1
            t_cnt = cnt
            for s2 in range(N-1):
                cnt = t_cnt
                suma2 = 0
                if N-1< 24-x +s2:
                    break
                for i in range(s2,s2+24-x):
                    cnt += 1
                    suma2 += t2[i]
                l = PrimeDivList(suma1+suma2)
                if len(l) == 1 and l[0] != suma1+suma2:
                    print(suma1+suma2)
                    return True
    return False
                
                
            


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

#?def ex5(t):
#Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
#funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
#nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
#figury była równa zero. #! lista krotek wszystkich mozliwych króli w rzędzie - można zapisać to jako 2 wymiarową

def ex6(t1,t2):
#Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
#sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
#iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.
    N = len(t1)
    for x in range(1,N): #długość wycinków
        for s1 in range(N-1): #s - start - 1st index wycinka
            if s1+x >= N:
                break
            suma1 = 0
            cnt = 0
            for i in range(s1,s1+x):
                suma1 += t1[i]
                cnt += 1
            t_cnt = cnt
            for s2 in range(N-1):
                if s2+x >= N:
                    break
                cnt = t_cnt
                suma2 = 0
                for i in range(s2,s2+x):
                    cnt += 1
                    suma2 += t2[i]
                l = PrimeDivList(suma1+suma2)
                if len(l) == 2 and l[0]*l[1] == suma1+suma2:
                    return True
    return False

def ex7(t):
#Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
#można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy był wielokrotnością
#(co najmniej dwukrotnością) dowolnej liczby naturalnej większej od 1.
    N = len(t)
    for x in range(N):
        for y in range(N):
            for z in range(y+1,N):
                flag = True
                for r in range(N):
                    if r == x:
                        continue
                    for c in range(N):
                        if c == z or c == y:
                            continue
                        if ((t[r][c]**0.5)*10) % 10 != 0:
                            flag = False
                            break
                if flag == True:
                    return True
    return False

def magmino(t,a=0,i=0,f=False,length=1):
    global maxi
    if i == 0:
        return magmino(t,t[i+1][0],i+1) or magmino(t,t[i+1][1],i+1)
    if i == len(t)-1:
        return None
    if f == True and (a == t[i][0] or a == t[i][1]):
        tmp = t[i]
        del t[i]
        t.insert(0,tmp)
        if length > maxi:
            maxi = length
        if a == t[0][0]:
            return magmino(t,t[i+1][1],i+1,True,length + 1) or magmino(t,t[i+1][1],i+1,False,length)
        elif a == t[0][1]:
            return magmino(t,t[i+1][0],i+1,True,length + 1) or magmino(t,t[i+1][1],i+1,False,length)
    else:
        return magmino(t,t[i+1][0],i+1,True) or magmino(t,t[i+1][1],i+1,True) or magmino(t,t[i+1][0],i+1,False) or magmino(t,t[i+1][1],i+1,False)

def ex8(t):
#Najdłuższy ciąg magmino
    magmino(t)
    for j in range(1,len(t)):
        tmp = t[j]
        del t[j]
        t.insert(0,tmp)
        magmino(t)

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
    t = [(2,8),(0,1),(2,3),(3,6),(2,6),(3,4),(6,7),(2,9)]
    maxi = 1
    ex8(t)
    print(maxi)