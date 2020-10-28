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
    N = int(input("podaj N: "))
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
    
    print(l_N)

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

#################################################

def czy_pierwsza(n):
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    k = 2
    while(k*k<=n):
        if(n%k==0):
            return False
        k+=1
    return True

def ex8():
#Zadanie 8. Dana jest N-elementowa tablica t zawierajaca liczby naturalne. W tablicy mozemy przeskoczyc
#z pola o indeksie k o n pól w prawo jezeli wartosc n jest czynnikiem pierwszym liczby t[k]. Napisac funkcje
#sprawdzajaca czy jest mozliwe przejscie z pierwszego pola tablicy na ostatnie pole.

    ta = [20, 150, 2, 200, 300, 195, 14, 15, 3, 3, 18, 21, 300, 3, 6, 3, 5, 12, 1]
    z = len(ta)


    tb = [False]*z #tablica przechowuje informacje czy mozna na to pole wskoczyć z pierwszego pola
    tb[0] = True

    for i in range(z):
        if(tb[i]==True):
            k=2
            num = ta[i] #przypisuje liczbe z pola o indeksie i
            while(k<=num and k<z-i):
                if(num%k==0):
                    if(czy_pierwsza(k)):
                        tb[i+k]=True
                k=k+1

    print(tb[z-1])

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

    N = 100 #int(input("N: "))
    t = [5,1,8,10,3,9,5]#[ randint(1,100) for i in range(N)]
    q = 1
    temp = 1
    max = 0

    print(t)

    for i in range(1,len(t)):
        q = t[i] / t[i-1]
        j = i
        while j < len(t) and t[j-1] * q == t[j]:
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

    N = 100 #int(input("N: "))
    t = [0]*N
    
    for i in range(len(t)):
        while t[i] % 2 == 0:
            t[i] = randint(1,99)
    
#niedokończone bo się nie chciało

def ex13():
#Zadanie 13. Prosze napisac program, który wypełnia N-elementowa tablice t trzycyfrowymi liczbami
#pseudolosowymi, a nastepnie wyznacza i wypisuje długosc najdłuzszego podciagu spójnego znajdujacego
#sie w tablicy dla którego w tablicy wystepuje równiez rewers tego ciagu. Na przykład dla tablicy: t=
#[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzia jest liczba 4.
    from random import randint

    N = int(input("N: "))
    t = [0]*N
    N = len(t) 
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
        
            



#def ex14():
#Zadanie 14. Napisac program wyznaczajacy na drodze eksperymentu prawdopodobienstwo tego, ze w
#grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły sie tego samego dnia roku. Wyznaczyc
#wartosci prawdopodobienstwa dla N z zakresu 20-40.



if __name__ == "__main__":
    #string_compare("wdfwdwd","wdfrwerw")
    ex13()
