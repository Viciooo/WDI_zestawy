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
    N = 1000
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

    print("2.", suma // 10, sep ='')
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

#powinno być podane że czy
    from random import randint
    N = 5
    t = [0] * N

    for i in range(N):
        t[i] = randint(2,10)
        i += 1
    print(t)
    #step = 0





if __name__ == "__main__":
    ex4()
