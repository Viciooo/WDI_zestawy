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
    #tmp = 0
    for r in range(1,len(t)):
        #j = r
        while r > 0 and t[r][0] < t[r-1][0]:
            t[r-1], t[r] = t[r], t[r-1]
            r -= 1
    return t

def ex6(t,T2):
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
                continue

        elif len(t[1]) == 0:
                del t[1]
                continue

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

def SearchForMaxIn2DmTab(t):
    el_max = 0
    for r in range(len(t)):
        for c in range(len(t)):
            if t[r][c] > el_max:
                el_max = t[r][c]
    return el_max

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

def SearchForMini(t):
    mini = 1000
    for i in range(len(t)):
        if t[i][0] < mini:
            mini = t[i][0]
            index = i
    if len(t[index]) == 1:
        del t[index]
    else:
        del t[index][0]
    
    return mini

def ex7(T1,T2): #próbuję sposób z pivotem
#Zadanie 7. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
#M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane niemalejaco (w obrebie wiersza) liczby
#naturalne. Prosze napisac funkcje przepisujaca wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
#T2 były uporzadkowane niemalejaco.
    N = len(T1)
    for i in range(N*N):
        T2[i] = SearchForMini(T1)
    return T2

def ex8(t):
#Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
#poszukuje w tablicy najdłuzszego ciagu geometrycznego lezacego ukosnie w kierunku prawo-dół, liczacego
#co najmniej 3 elementy. Do funkcji nalezy przekazac tablice. Funkcja powinna zwrócic informacje czy udało
#sie znalezc taki ciag oraz długosc tego ciagu.
    N = len(t)
    r = 0
    c = 0
    cnt = 2
    while N-r >= 3:
        if N-c < 3:
            r += 1
            continue
        k = 1
        l = [0]*N
        i = 2
        l[0] = t[r][c]
        l[1] = t[r+k][c+k]
        if t[r][c] < t[r+k][c+k]:

            q = t[r+k][c+k] / t[r][c]  

            while r+k+1 < N and c+k+1 < N and (t[r+k+1][c+k+1])/(t[r+k][c+k]) == q:
                l[i] = t[r+k+1][c+k+1]
                i += 1
                if cnt < i:
                    cnt = i
                k += 1
                print(l)

        elif t[r][c] >= t[r+k][c+k]:

            q = t[r][c] / t[r+k][c+k]  

            while r+k+1 < N and c+k+1 < N and t[r+k][c+k]/t[r+k+1][c+k+1]== q:
                l[i] = t[r+k+1][c+k+1]
                i += 1
                if cnt < i:
                    cnt = i
                k += 1
                print(l)

        c += 1
    if cnt == 2:
        return 0
    return cnt


def ex9(t,k):
#Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
#poszukuje w tablicy kwadratu o liczbie pól bedacej liczba nieparzysta wieksza od 1, którego iloczyn 4 pól
#naroznych wynosi k. Do funkcji nalezy przekazac tablice i wartosc k. Funkcja powinna zwrócic informacje
#czy udało sie znalezc kwadrat oraz współrzedne (wiersz, kolumna) srodka kwadratu.
    x = 3
    N = len(t)
    while x <= N:
        r = 0
        c = 0
        while r+x <= N and c+x <= N:
            iloczyn = t[r][c]*t[r][c+x-1]*t[r+x-1][c]*t[r+x-1][c+x-1]
            if iloczyn == k:
                print("(",c+(x//2),",",r+(x//2),")",sep='')
                return True
            c += 1
            if c+x > N:
                c = 0
                r += 1
        x += 2
    return False

def ex10(T):
#Zadanie 10. Napisac funkcje która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartosc
#True w przypadku, gdy w kazdym wierszu i kazdej kolumnie wystepuje co najmniej jedno 0 oraz wartosc
#False w przeciwnym przypadku.
    N = len(T)
    col = [0]*N
    row = [0]*N    
    for r in range(N):
        for c in range(N):
            if T[r][c] == 0:
                col[c], row[r] = 1, 1
    print(col,row)
    for j in range(N):
        if col[j] == 0 or row[j] == 0:
            return False
    return True

def ConvertToOccurenceTab(n):
    tab = [0]*10
    while n != 0:
        tab[n%10] = 1
        n //= 10
    return tab

def ex11(t):
#Zadanie 11. Dwie liczby naturalne sa „przyjaciółkami jezeli zbiory cyfr z których zbudowane sa liczby
#sa identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
#naturalnymi. Prosze napisac funkcje, która dla tablicy T zwraca ile elementów tablicy sasiaduje wyłacznie z
#przyjaciółkami
    N = len(t)
    cnt = 0

    for r in range(N):
        for c in range(N):
            tab1 = ConvertToOccurenceTab(t[r][c])
            if r > 0:
                tab2 = ConvertToOccurenceTab(t[r-1][c])
                if tab2 != tab1:
                    continue
            if r < N-1:
                tab2 = ConvertToOccurenceTab(t[r+1][c])
                if tab2 != tab1:
                    continue
            if c > 0 and r > 0:
                tab2 = ConvertToOccurenceTab(t[r-1][c-1])
                if tab2 != tab1:
                    continue
            if c > 0 and r < N-1:
                tab2 = ConvertToOccurenceTab(t[r+1][c-1])
                if tab2 != tab1:
                    continue
            if c < N-1 and r > 0:
                tab2 = ConvertToOccurenceTab(t[r-1][c+1])
                if tab2 != tab1:
                    continue
            if c < N-1 and r < N-1:
                tab2 = ConvertToOccurenceTab(t[r+1][c+1])
                if tab2 != tab1:
                    continue
            cnt += 1

    return cnt

def IfComplex(n): #sprawdza czy złożona
    if n <=1:
        return 0
    if n ==2 or n ==3:
        return 0
    if n %2==0 or n%3==0:
        return 1
    i = 6
    while (i-1)**2<=n:
        if n %(i-1) == 0:
            return 1
        if n%(i+1) == 0:
            return 1
        i+=6
    return 0

def ex12(t):
#Zadanie 12. Dana jest tablica T[N][N][N]. Prosze napisac funkcje, do której przekazujemy tablice wypełniona
#liczbami wiekszymi od zera. Funkcja powinna zwracac wartosc True, jezeli na wszystkich poziomach
#tablicy liczba elementów sasiadujacych (w obrebia poziomu) z co najmniej 6 liczbami złozonymi jest jednakowa
#albo wartosc False w przeciwnym przypadku.
    N = len(t)
    tab = [0]*N
    for p in range(N):
        for r in range(N):
            for c in range(N):
                cnt = 0
                if r > 0:
                    cnt += IfComplex(t[p][r-1][c])
                if r < N-1:
                    cnt += IfComplex(t[p][r+1][c])
                if c > 0 and r > 0:
                    cnt += IfComplex(t[p][r-1][c-1])
                if c > 0 and r < N-1:
                    cnt += IfComplex(t[p][r+1][c-1])
                if c < N-1 and r > 0:
                    cnt += IfComplex(t[p][r-1][c+1])
                if c < N-1 and r < N-1:
                    cnt += IfComplex(t[p][r+1][c+1])
                if cnt >= 6:
                    tab[p] += 1
        if p != 0 and tab[p] != tab[p-1]:
            return False

    return True

def ex13(t): # linearyzujemy tablicę - bardzo fajny sposób
#Zadanie 13. Liczby naturalne a,b sa komplementarne jezeli ich suma jest liczba pierwsza. Dana jest tablica
#T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która zeruje elementy nie posiadajace
#liczby komplementarnej.
    N = len(t)
    for n1 in range(N**2): #to co sprawdzamy
        r1 = (n1)//N
        c1 = (n1)%N
        komplementarna = False
        for n2 in range(N**2): #czym sprawdzamy
            if n1 == n2:
                continue
            r2 = (n2)//N
            c2 = (n2)%N
            if IfPrime(t[r1][c1] + t[r2][c2]) == True:
                komplementarna = True               
        if komplementarna == False:
            t[r1][c1] = 0
    return t

def CntOddDiv(n):
    cnt = 0 #jeśli zniszczy n to będziemy dzielić tmp
    while n != 0:
        if n % 2 == 1:
            cnt += 1
        n //= 2
    return cnt

def ConvertToAmountOf1Tab(t):
    N = len(t)
    tab = [0]*N
    for i in range(N):
        tab[i] = [0]*N
    for r in range(N):
        for c in range(N):
            tab[r][c] = CntOddDiv(t[r][c])
    return tab

def ex14(T1,T2):
#Zadanie 14. Dwie liczby naturalne sa zgodne jezeli w zapisie dwójkowym zawieraja te sama liczbe jedynek,
#np. 22 = 10110 i 14 = 1110. Dane sa tablice T1[N1][N1] T2[N2][N2], gdzie N2>=N1. Prosze napisac funkcje,
#która sprawdza czy istnieje takie połozenie tablicy T1 wewnatrz tablicy T2, przy którym liczba zgodnych
#elementów jest wieksza od 33%. Do funkcji nalezy przekazac tablice T1 i T2. Obie oryginalne tablice powinny
#pozostac nie zmieniane.
    N1 = len(T1)
    r1 = 0 
    c1 = 0
    N2 = len(T2)
    r2 = 0 
    c2 = 0
    tab1 = ConvertToAmountOf1Tab(T1) 
    tab2 = ConvertToAmountOf1Tab(T2)
    for r2 in range(N2-N1):
        for c2 in range(N2-N1):
            zgodnosc = 0
            for r1 in range(N1):
                for c1 in range(N1):
                    if tab1[r1][c1] == tab2[r1+r2][c1+c2]:
                        zgodnosc += 1
            if zgodnosc > (N1*N1)/3:
                return True
    return False

#!!def ex15(T):
#Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
#odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym kazda liczba zawiera co najmniej jedna cyfre
#bedaca liczba pierwsza?


def GenRndTabOfGrowingInts(N,start,end):
    from random import randint
    t = [0]*N
    x = 0
    iterator = end // N
    y = x + iterator
    for i in range(N):
        t[i] = randint(x,y)
        x += iterator
        y += iterator
    return t

def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])
if __name__ == "__main__":
    T1 = GenRnd2DmArr(3,10,50)
    T2 = GenRnd2DmArr(7,10,50)
    print(ex14(T1,T2))
