#Moduł przydatnych funkcji

def Split(word): #dzieli string na znaki 
    return [char for char in word]

def StringCompare(string1,string2): #porównywanie stringów
    
    cnt = 0
    l1 = split(string1)
    l2 = split(string2)

    print(l1,l2)

    if len(l1) > len(l2):
        length = len(l1)
    else:
        length = len(l2)

    for i in range(length):
        if l1[i] != l2[i]:
            break
        print(">>", cnt)
        cnt += 1

    print("Są podobne do :", cnt, "miejsca")

def InsertionSort(arr): #sortowanie
    for i in range(1, len(arr)):  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

def GenRndTab(length,start,end): #generuje tablicę jednowymiarową
    from random import randint
    tab = []
    for i in range(length):
        tab.append(randint(start,end))
    return tab

def IfPrime(n): #sprawdza czy pierwsza
    k = 2

    if(n==1):
        return False

    while k <= n**0.5:

        if n % k == 0:

            if n // k == 1:
                return True
            else:
                return False
        k += 1

    return True

def ToBinary(n,length):#zamienia liczbę na binarną 
    l =[]
    while n // 2 != 0:
        l.append(n%2)
        n //=2
    l.append(n%2)
    while len(l)<length:
        l.append(0)
    return l

def DivList(n): #zwraca listę podzielników w postaci tablicy
    l = []
    for i in range(2,n+1):
        if n % i == 0:
            l.append(i)
        while n % i == 0:
            n //= i
    return l

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

def RowSum(tab): #sumuje wiersze
    N = len(tab)
    suma = 0
    for i in range(N):
        suma += tab[i]
    return suma

def FlipTheTab(tab): #obraca tablicę kolumny to teraz wiersze itd
    r = 0 
    c = 0
    y = 0
    suma = 0
    N = len(tab)
    new_tab = [0]*N

    for i in range(N):
        new_tab[i] = N*[0]
    for c in range(N):
        x = 0
        for r in range(N):
            new_tab[y][x] = tab[r][c]
            x += 1
        y += 1
    return new_tab

def SearchForBorS(tab,bORs): # biggest or smallest - szuka największego lub najmniejszego el tablicy
    N = len(tab)
    i_saver = 0
    val_saver = tab[0]
    if bORs == "b":
        for i in range(1,N):
            if tab[i] > val_saver:
                 i_saver = i
                 val_saver = tab[i]
    if bORs == "s":
        for i in range(1,N):
            if tab[i] < val_saver:
                 i_saver = i
                 val_saver = tab[i]
    return i_saver
