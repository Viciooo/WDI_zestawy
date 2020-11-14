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

def ToBinary(n,length):#zamienia liczbę na binarną 
    l =[]
    while n // 2 != 0:
        l.append(n%2)
        n //=2
    l.append(n%2)
    while len(l)<length:
        l.append(0)
    return l

def PrimeDivList(n): #zwraca listę podzielników pierwszych w postaci tablicy
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
def TwoDimCopy(t): #copy of 2 dimentional list/array idk
    l = len(t)
    new_tab = [[0]*l]*l
    i,j = 0,0
    for row in t:
        for column in row:
            new_tab[i][j] = column
            j+=1
        i+=1
    return new_tab
def OneDimCopy(t): # copy of 1 dimentioanl array/list
    new_tab = [0]*(len(t))
    i = 0
    for elem in t:
        new_tab[i] = elem
        i+=1
def Otoczka(t): # 0 dookola 2 dim array
    n = len(t)
    for n in t:
        n.insert(0,0)
        n.append(0,0)
    t.insert(0,[0]*(n+2))
    t.append([0]*(n+2))