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
        cnt += IfMadeOfOddDigits(t[i])   
    if cnt == N:
        return True
    return False

def IfHasOneEvenDigit(tab):
    cnt = 0
    for i in range(len(tab)):
        if tab[i] == 0:
            cnt += 1
        while tab[i] % 10 != 0:
            tmp = tab[i] % 10
            if tmp % 2 == 0:
                cnt += 1
                break
            tab[i] //= 10
    return cnt

def ex3(t):
#Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
#odpowiada na pytanie, czy istnieje wiersz w tablicy w którym kazda z liczb zawiera przynajmniej jedna cyfre
#parzysta. 

    N = len(t)
    cnt = 0  
    for i in range(len(t)):
        cnt = 0
        cnt += IfHasOneEvenDigit(t[i])
        if cnt == N:
            return True 
    return False

def RowSum(tab):
    N = len(tab)
    suma = 0
    for i in range(N):
        suma += tab[i]
    return suma

def FlipTheTab(tab):
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

def SearchForBorS(tab,bORs): # biggest or smallest
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

def ColumnSum(t,c):
    columns = 0
    for r in range(len(t)):
        columns += t[r][c]
    return columns

def ex4(t):
#Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
#zwraca wiersz i kolumne dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym lezy
#element do sumy elementów wiersza w którym lezy element jest najwieksza.
    N = len(t)
    columns = [0]*N
    rows = [0]*N

    for i in range(N):
        rows[i] = RowSum(t[i])
        columns[i] = ColumnSum(t,i)
    #szukamy el największego z columns i el najmniejszy z rows
    print("[",SearchForBorS(rows,"s"),"]","[",SearchForBorS(columns,"b"),"]", sep = '')
    return

def ex5(t): 
#Zadanie 5. Poprzednie zadanie z tablica wypełniona liczbami całkowitymi.    
    N = len(t)
    columns = [0]*N
    rows = [0]*N

    for i in range(N):
        rows[i] = RowSum(t[i])
        columns[i] = ColumnSum(t,i)
    #szukamy el największego z columns i el najmniejszy z rows
    index = 0
    while rows[index] == 0:
        index += 1
    max_wynik = columns[0] / rows[index]
    col = 0
    row = 0
    for j in range(N):
        for i in range(N):
            if rows[i] != 0:
                wynik = columns[j] / rows[i]
                if wynik > max_wynik:
                    max_wynik = wynik
                    col = j
                    row = i 

    print("[",row,"]","[",col,"]", sep = '')

def Convert2DmTo1Dm(t): #zapisuje dwuwymiarową wiersz po wierszu jako jednowymiarową
    N = len(t)
    tab = []
    for x in range(N):
        for y in range(N):
            tab.append(t[x][y])
    return tab

def Uniq(tab): #zwraca tablicę z elementami, które się nie powtarzają w tablicy którą przetwarza
    i = 0
    N = len(tab)
    tab.sort()
    while i+1 < len(tab):
        duplikat = False
        while i+1 < len(tab) and tab[i] == tab[i+1]:
            del tab[i+1]
            duplikat = True
        if duplikat == True:
            del tab[i]
        if duplikat == False:  
            i += 1
    for i in range(N):
        tab.append(0)
    return tab

def RowsByFirstIndexSort(t):
    tmp = 0
    for r in range(1,len(t)):
        j = r
        while r > 0 and t[r][0] < t[r-1][0]:
            t[r-1], t[r] = t[r], t[r-1]
            r -= 1
    return t

def ex6(t,T2):
#nieoptymalna wersja - sortuje el posortowane
#Zadanie 6. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
#M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane rosnaco (w obrebie wiersza) liczby
#naturalne. Prosze napisac funkcje przepisujaca wszystkie singletony (liczby wystepujace dokładnie raz) z
#tablicy T1 do T2, tak aby liczby w tablicy T2 były uporzadkowane rosnaco. Pozostałe elementy tablicy T2
#powinny zawierac zera.

    tmp = -1
    i = 0

    while len(t) > 1:

        if len(t[0]) == 0:
                del t[0]

        elif len(t[1]) == 0:
                del t[1]

        t = RowsByFirstIndexSort(t)

        if t[0][0] == tmp:
            del t[0][0] 

        elif t[1][0] == t[0][0]:
            tmp = t[0][0]
            del t[0][0],t[1][0]

        else:
            T2[i] = t[0][0]
            del t[0][0]

            if len(t[0]) == 0:
                del t[0]

            i += 1

    for j in range(len(t[0])):
        T2[i] = t[0][j]
        i += 1

    return T2

#def ex7():
#Zadanie 7. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
#M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane niemalejaco (w obrebie wiersza) liczby
#naturalne. Prosze napisac funkcje przepisujaca wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
#T2 były uporzadkowane niemalejaco.
    

#def ex8():
#Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
#poszukuje w tablicy najdłuzszego ciagu geometrycznego lezacego ukosnie w kierunku prawo-dół, liczacego
#co najmniej 3 elementy. Do funkcji nalezy przekazac tablice. Funkcja powinna zwrócic informacje czy udało
#sie znalezc taki ciag oraz długosc tego ciagu.

def GenTabOfRndGrowingInts(N,start,end):
    from random import randint
    t = [0]*N
    tmp = start
    for i in range(N):
        start = tmp
        t[i] = [0]*N
        for j in range(N):
            t[i][j] = randint(start,end)
            start = t[i][j] + 1
    return t

def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])
if __name__ == "__main__":
    #t = GenTabOfRndGrowingInts(3,10,100)
    #T2 = [0]*4**2
    #T2 = ex6(t,T2)
    #print(T2)
    #Print2DmTab(t)
