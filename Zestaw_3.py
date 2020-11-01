def split(word): 
    return [char for char in word]

def string_compare(string1,string2):
    
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


def ex1():
#Zadanie 1. Napisac funkcje zamieniajaca i wypisujaca liczbe naturalna na system o podstawie 2-16.
    n = int(input("n: "))
    coding = int(input("coding: "))
    i = 0
    l_n = []
    while n != 0:
        if n % coding < 10:
            l_n.append(n % coding)
        else:
            l_n.append(chr(n % coding + 55))
        n //= coding
    l_n = l_n[::-1]

    i = 0
    for i in range(len(l_n)):
        print(l_n[i], end = "") 

def ex2():
#Zadanie 2. Napisac program wczytujacy dwie liczby naturalne i odpowiadajacy na pytanie czy sa one
#zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
    x = int(input("x: "))
    y = int(input("y: "))

    if len(str(x)) != len(str(y)): #to można ominąć - celem jest tylko instant wykluczenie 
        return False
    
    l_x = [0]* 10
    l_y = [0]* 10
    
    while x != 0:
        l_x[x % 10] += 1
        x //= 10

        l_y[y % 10] += 1
        y //= 10
    
    if l_x == l_y:
        return True
    else:
        return False
    

def ex3():
#Zadanie 3. Napisac program generujacy i wypisujacy liczby pierwsze mniejsze od N metoda Sita Eratostenesa.
    '''N = int(input("podaj N: "))
    l_N = []
    x = 0

    for i in range(2,N+1):
        l_N.append(i)
       
    while l_N[x] <= N**(0.5):
        y = x + 1
        while y < len(l_N):
            if l_N[y] % l_N[x] == 0:
                del l_N[y]
            y += 1
        x += 1
    
    print(l_N)'''

def ex4():
#Zadanie 4. Napisac program obliczajacy i wypisujacy stała e z rozwiniecia w szereg e = 1/0! + 1/1! +
#1/2! + 1/3! + ... z dokładnoscia N cyfr dziesietnych (N jest rzedu 1000)
    '''from time import time
    start = time()
    N = 1000
    el_amt = 1000
    l_e = [0] * el_amt
    i = 1
    l_e[0] = 1
    suma = 0

    while i < el_amt:
        l_e[i] = l_e[i-1] * i
        i += 1

    for i in range(2,el_amt):
        div = 1 % l_e[i]
        j = 0
        l_l = [0] * N

        for j in range(N):
            div *= 10
            if (div // l_e[i]) != 0:
                l_l[j] += (div // l_e[i])
            div = div % l_e[i]

        for k in range(len(l_l)):
            suma += l_l[k] * 10**(N-k)'''
    from time import time
    start = time()

    N = 1000
    el_amt = 1000
    i = 1
    suma = 0
    sil = 1
    for i in range(2,el_amt):
        sil *= i
        div = 1 % sil
        j = 0
        l_l = [0] * N
        for j in range(N):
            div *= 10
            if (div // sil) != 0:
                l_l[j] += (div // sil)
            div = div % sil

        for k in range(len(l_l)):
            suma += l_l[k] * 10**(N-k)

    print("2.", suma // 10, sep ='')

    end = time()
    print(end - start)
            

    
def ex5_1(): # GDYBYŚMY CHCIELI NIE ZDAĆ
#Zadanie 5. Napisac program, który wczytuje wprowadzany z klawiatury ciag liczb naturalnych zakonczonych
#zerem stanowiacym wyłacznie znacznik konca danych. Program powinien wypisac 10 co do wielkosci
#wartosc, jaka wystapiła w ciagu. Mozna załozyc, ze w ciagu znajduje sie wystarczajaca liczba elementów.
    temp = 1
    l_list = []
    while temp != 0:
        temp = int(input("> "))
        if temp != 0:
            l_list.append(temp) #zamiast append można wygenerować tablicę zer i wpisać na kolejne miejsca w pętli używając 'i' następujące elementy
#wtedy generujemy listę np 100 zer i po skończonym wpisywaniu ucinamy el = 0
    print(l_list)
    l_list.sort()
    print(l_list[9])


def insertionSort(arr): 
    for i in range(1, len(arr)):  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

def ex5():
#Zadanie 5. Napisac program, który wczytuje wprowadzany z klawiatury ciag liczb naturalnych zakonczonych
#zerem stanowiacym wyłacznie znacznik konca danych. Program powinien wypisac 10 co do wielkosci
#wartosc, jaka wystapiła w ciagu. Mozna załozyc, ze w ciagu znajduje sie wystarczajaca liczba elementów.
    temp = 1
    ciag_max = 20
    l_list = [0] * ciag_max
    i = 0
    x = 0

    while temp != 0:
        temp = int(input("> "))
        l_list[i] = temp
        i += 1

    while x < len(l_list):
        if l_list[x] == 0:
            del l_list[x]
            x -= 1
        else:
            x += 1

    insertionSort(l_list)
    print(l_list[9])

def ex6():
#Zadanie 6. Napisac program wypełniajacy N-elementowa tablice t liczbami naturalnymi 1-1000 i sprawdzajacy
#czy kazdy element tablicy zawiera co najmniej jedna cyfre nieparzysta.
    from random import randint

    #Robię to trochę nie szablonowo. Nie wypisuję całej tablicy tylko dynamicznie za każdym razem sprawdzam czy
    #bieżący element spełnia założenia - jeśli nie to wychodzę z programu i zwracam false gdyż program ma podawać 
    #czy każdy element zawiera co najmniej jedną cyfrę nieparzystą, więc jak znajdę jeden, który nie ma to zbędne jest szukanie dalej

    N = 10
    t = [0] * N

    for i in range(N):
        bOdd = False
        t[i] = randint(1,1000)
        num = t[i]
        print(t)
        while num != 0:
            temp = num % 10
            if temp % 2 == 1:
                bOdd = True
                break
            num //= 10
        if bOdd == False:
            return False
        i += 1

    return True

def ex7():
#Zadanie 7. Napisac program wypełniajacy N-elementowa tablice t liczbami naturalnymi 1-1000 i sprawdzajacy
#czy istnieje element tablicy zawierajacy wyłacznie cyfry nieparzyste.
    from random import randint
    N = 10
    t = [0] * N


    for i in range(N):
        odd_cnt = 0
        length = 0
        t[i] = randint(1,1000)
        num = t[i]
        print(t)
        while num != 0:
            temp = num % 10

            if temp % 2 == 1:
                odd_cnt += 1

            num //= 10
            length += 1

        if odd_cnt == length:
            return True

        i += 1

    return False

def ex8():
#Zadanie 8. Dana jest N-elementowa tablica t zawierajaca liczby naturalne. W tablicy mozemy przeskoczyc
#z pola o indeksie k o n pól w prawo jezeli wartosc n jest czynnikiem pierwszym liczby t[k]. Napisac funkcje
#sprawdzajaca czy jest mozliwe przejscie z pierwszego pola tablicy na ostatnie pole.
    l_num = [2,3,6,4,1,1]
    l_zer = len(l_num)* [0]
    l_zer[0] = 1
    i = 0

    while i < len(l_num):
        l_div = div_check(l_num[i])
        j = i
        if l_zer[i] == 1:
            while j < len(l_zer):
                if l_zer[j] == 1:
                    for k in l_div:
                        if j+k < len(l_zer):
                            l_zer[j+k] = 1
                j += 1
        i += 1
    print(l_zer)
    if l_zer[-1] == 1:
        return True
    else:
        return False

def ex9():
#Zadanie 9. Napisac funkcje, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długosc najdłuzszego, spójnego podciagu rosnacego.   
    from random import randint
    N = int(input("N: "))
    t = [ randint(1,100) for i in range(N)]
    max = 0
    temp = 1

    for i in range(1,len(t)):
        if t[i-1] < t[i]:
            temp += 1
        else:
            if temp > max:
                max = temp
            temp = 1
    print(t)
    print(max)

def ex10():
#Zadanie 10. Napisac funkcje, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długosc najdłuzszego, spójnego podciagu arytmetycznego.
    from random import randint

    N = 100 #int(input("N: "))
    t = [2,4,6,10,1,3,5]#[ randint(1,100) for i in range(N)]
    diff = 0
    temp = 1
    max = 0

    print(t)

    for i in range(1,len(t)):
        diff = t[i] - t[i-1]
        j = i
        while j < len(t) and t[j-1] + diff == t[j]:
            temp += 1
            j += 1
        if temp > max:
            max = temp
        temp = 1

    print(max)


def ex11():
#Zadanie 11. Napisac funkcje, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długosc najdłuzszego, spójnego podciagu geometrycznego.
    from random import randint

    N = int(input("N: "))
    t = [ randint(1,100) for i in range(N)]
    q = 1
    temp = 1
    max = 0

    for i in range(1,len(t)):
        q = t[i-1] / t[i]
        j = i
        while j < len(t) and t[j-1] == t[j] * q:
            temp += 1
            j += 1
        if temp > max:
            max = temp
        temp = 1

    print(max)

def ex12():
#Zadanie 12. Prosze napisac program, który wypełnia N-elementowa tablice t pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a nastepnie wyznacza i wypisuje róznice pomiedzy długoscia najdłuzszego
#znajdujacego sie w niej ciagu arytmetycznego o dodatniej róznicy, a długoscia najdłuzszego ciagu arytmetycznego
#o ujemnej róznicy, przy załozeniu, ze kolejnymi wyrazami ciagu sa elementy tablicy o kolejnych
#indeksach.
    from random import randint

    N = int(input("N: "))
    t = [0]*N
    max_m = 0
    max_p = 0
    cnt_p = 0
    cnt_m = 0
    
    for i in range(N):
        while t[i] % 2 == 0:
            t[i] = randint(1,99)
    
    print(t)

    for i in range(1,N):
        if t[i-1] > t[i]: #malejący
            r_m = t[i-1] - t[i]
            cnt_m = 1
            j = i
            while j+1 < N and t[j] - r_m == t[j+1]:
                cnt_m += 1
                j += 1

        if t[i-1] < t[i]: #rosnący
            r_p = t[i] - t[i-1]
            cnt_p = 1
            j = i
            while j+1 < N and t[j] + r_p == t[j+1]:
                cnt_p += 1
                j += 1
        if cnt_m > max_m:
            max_m = cnt_m
        if cnt_p > max_p:
            max_p = cnt_p
        
    print("wynik",abs(max_m-max_p))

def ex13():
#Zadanie 13. Prosze napisac program, który wypełnia N-elementowa tablice t trzycyfrowymi liczbami
#pseudolosowymi, a nastepnie wyznacza i wypisuje długosc najdłuzszego podciagu spójnego znajdujacego
#sie w tablicy dla którego w tablicy wystepuje równiez rewers tego ciagu. Na przykład dla tablicy: t=
#[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzia jest liczba 4.
    from random import randint

    N = int(input("N: "))
    t = [0]*N
    m_cnt = 1
    
    for i in range(len(t)):
        t[i] = randint(100,999)
    
    for i in range(1,N):
        j = i
        k = 1
        cnt = 1
        while j < N:
            if t[i-1] == t[j] and t[i] == t[j-1]:
                cnt += 1
                while t[i+k] == t[j-1-k]:
                    cnt +=1
                    k += 1
            j += 1

        if cnt > m_cnt:
           m_cnt = cnt

    print(t)
    print(m_cnt)
        
            



def ex14():
#Zadanie 14. Napisac program wyznaczajacy na drodze eksperymentu prawdopodobienstwo tego, ze w
#grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły sie tego samego dnia roku. Wyznaczyc
#wartosci prawdopodobienstwa dla N z zakresu 20-40.
    from random import randint
    N = 23
    t = [0]* N
    cnt = 0
    for i in range(100): # 100 razy sprawdzamy tą sytuację i wynik podamy wtedy w procentach
        for x in range(N): # generowanie losowej tablicy
            t[x] = randint(1,365)
        for j in range(N-1): #sprawdzanie dla każdego elementu tablicy czy gdziesz w tablicy jest element mu równy
            k = j + 1
            while k + 1 < N and t[j] != t[k]:
                k += 1
            if t[j] == t[k]:
                cnt += 1
                break
    
    print("Szanse na to wynoszą", cnt, "%")


def gen_rnd_tab(length,start,end):
    from random import randint
    tab = []
    for i in range(length):
        tab.append(randint(start,end))
    return tab

def czy_pierwsza(n):
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

def ex15():
#Zadanie 15. Dana jest duza tablica t. Prosze napisac funkcje, która zwraca informacje czy w tablicy
#zachodzi nastepujacy warunek: „wszystkie elementy, których indeks jest elementem ciagu Fibonacciego sa
#liczbami złozonymi, a wsród pozostałych przynajmniej jedna jest liczba pierwsza”
    N = 100
    t = gen_rnd_tab(N,1,100)
    a1 = 1
    a2 = 1
    cnt = 0
    
    for i in range(N):
        if i == a2:
            a1, a2 = a2, a1+a2
            if czy_pierwsza(t[i]) == True:
                return False
        else:
            if czy_pierwsza(t[i]) == True:
                cnt += 1  
    if cnt > 0:
        return True
    
    return False

def ex16():
#Zadanie 16. Mamy zdefiniowana n-elementowa tablice liczb całkowitych. Prosze napisac funkcje zwracajaca
#wartosc typu bool oznaczajaca, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
#jeden element najwiekszy (liczba elementów najmniejszych oznacza liczbe takich elementów o tej samej
#wartosci).

    N = 100
    i = 0

    t = gen_rnd_tab(N,1,100)

    insertionSort(t)
    print(t)

    if t[0] == t[1]:
        return False
    if t[-1] == t[-2]:
        return False
    
    return True

def convert_to_bin(n,length):
    l =[]
    while n // 2 != 0:
        l.append(n%2)
        n //=2
    l.append(n%2)
    while len(l)<length:
        l.append(0)
    return l

def ex17(t1,t2):
#Zadanie 17. Dane sa dwie N-elementowe tablice t1 i t2 zawierajace liczby naturalne. Z wartosci w obu
#tablicach mozemy tworzyc sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
#tablicy t1 lub t2) o kazdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
#sumami sa na przykład 1+3+2+4, 9+7+4+8, 1+7+2+8, 1+9+7+2+4+8. Prosze napisac funkcje generujaca
#i wypisujaca wszystkie poprawne sumy, które sa liczbami pierwszymi. Do funkcji nalezy przekazac dwie
#tablice, funkcja powinna zwrócic liczbe znalezionych i wypisanych sum.    
    cnt = 0
    if len(t1) >= len(t2): #chcemy wiedzieć, która dłuższa bo robimy maskę do możliwie krótszej bo będziemy doklejać wyrazy z dłuższej za każdym razem
        mask = [0]*len(t2)  #zawsze ma długość krótszej z tablic
        tab1 = t1   #zawsze  dłuższa 
        tab2 = t2   #krótsza
        length = len(t2)
    else:
        mask = [0]*len(t1)
        tab1 = t2   #zawsze  dłuższa
        tab2 = t1   #krótsza
        length = len(t1)

    for j in range(2**length):
        suma1 = 0 #jeśli występuje coś z tab2 to nie ma tam z tab1 nic
        suma2 = 0 #są oba arg z indexu i z obu tablic
        i = 0
        mask = convert_to_bin(j,length)
        for i in range(len(mask)):
            if mask[i] == 1:
                suma1 += tab2[i]
                suma2 += tab2[i]
                suma2 += tab1[i]
            elif mask[i] == 0:
                suma1 += tab1[i]
            suma2 += tab1[i]
        if czy_pierwsza(suma1) == True:
            print("Suma1: ",suma1)
            cnt += 1
        if czy_pierwsza(suma2) == True and suma2 != suma1:
            print("Suma2: ",suma2)
            cnt += 1
            
    return cnt


def ex18(tab):
#Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Prosze napisac
#funkcje, która zwraca długosc najdłuzszego spójnego podciagu bedacego palindromem złozonym wyłacznie
#z liczb nieparzystych. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic długosc znalezionego
#podciagu lub wartosc 0 jezeli taki podciag nie istnieje.    
    length = len(tab)
    cnt = 1
    m_cnt = 1

    for i in range(1,length):
        cnt = 1
        k = 1
        if t[i] % 2 == 0:
            continue
        elif t[i] == t[i-1]:
            cnt += 1
            while i-1-k >= 0 and i+k <= length:
                if t[i+k]%2==0 or t[i-1-k]%2==0:
                    break
                if t[i+k] != t[i-1-k]:
                    break
                cnt += 2
                k += 1
        else:
            while i-k > 0 and i+k < length:
                if t[i+k]%2==0 or t[i-k]%2==0:
                    break
                if t[i+k] != t[i-k]:
                    break
                cnt += 2
                k += 1

        if cnt > m_cnt:
            m_cnt = cnt

    if m_cnt == 1:
        return 0
    
    else:
        return m_cnt

def ex19(tab):
#Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Prosze napisac funkcje,
#która zwraca długosc najdłuzszego, spójnego podciagu rosnacego dla którego suma jego elementów jest
#równa sumie indeksów tych elementów. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic długosc
#znalezionego podciagu lub wartosc 0 jezeli taki podciag nie istnieje.
    length = len(tab)
    i = 0
    m_cnt = 1

    while i < length:
        index_sum = i
        k = 0
        suma = tab[i]
        cnt = 1
        while i+k+1 < length and tab[i+k] < tab[i+k+1]: # sumujemy wyrazy i indexy wyrazów ciągów rosnących
            suma += tab[i+k+1]
            index_sum += i+k+1
            k += 1
            cnt += 1
        while k != 0 and index_sum != suma:
            suma -= tab[i+k]
            index_sum -= i+k
            k -= 1
            cnt -= 1
        if index_sum == suma and cnt > m_cnt:
            m_cnt = cnt
        i += 1
    
    if m_cnt == 1:
        return 0
    else:
        return m_cnt


def div_check(n):
    l = []
    for i in range(2,n+1):
        if n % i == 0:
            l.append(i)
        while n % i == 0:
            n //= i
    return l

def ex20(t):
#Zadanie 20. Dana jest N-elementowa tablica t zawierajaca liczby naturalne mniejsze od 1000. Prosze napisac
#funkcje, która zwraca długosc najdłuzszego, spójnego fragmentu tablicy, dla którego w iloczynie jego elementów
#kazdy czynniki pierwszy wystepuje co najwyzej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22]
#wynikiem jest wartosc 5.

    #używamy naszej funkcji div check jeśli po podzieleniu przez każdy z dzielników liczba jest != od 1 to odrzucamy ten iloczyn
    #iloczynu szukamy w następujący sposób:
    #1)  zaczynamy i'tego indexu i patrzymy na podzielniki iloczynu t[i]*t[i+k] jeśli iloczyn podzielony przez div check != 0 to 
    # zwiększam i o 1, jeśli == to cnt +=1 i k +=1
    #2)sprawdzam czy m_cnt < cnt jeśli tak to zamieniam wartość
    m_cnt = 1
    l = []

    for i in range(1,len(t)):
        k = 1
        cnt = 1
        iloczyn = t[i-1]*t[i]
        while i+k < len(t):
            l = div_check(iloczyn)
            for j in range(len(l)):
                iloczyn //= l[j]
            if iloczyn == 1:
                cnt += 1
                iloczyn *= t[i+k]
                k += 1
            else:
                break
        if m_cnt < cnt:
            m_cnt = cnt
    
    return m_cnt

if __name__ == "__main__":
    #N = 5 #int(input("N: "))
    #t = [2,23,33,35,7,4,6,7,5,11,13,22]#gen_rnd_tab(N,1,999)
    #N = len(t)
    #t1 = [i for i in range(N)] # list comprehension - bardzo fajne narzędzie
    #print(t)
    #print(t1)
    #print(ex20(t))
    #t1 = [2,3,1]#gen_rnd_tab(10,1,100)
    #t2 = [5,1,2]#gen_rnd_tab(10,1,100)
    #print(ex17(t1,t2))
