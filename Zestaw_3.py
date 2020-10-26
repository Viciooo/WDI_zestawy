def ex1():
#Zadanie 1. Napisac funkcje zamieniajaca i wypisujaca liczbe naturalna na system o podstawie 2-16.
    n = int(input("n: "))
    coding = 2
    i = 0
    l_n = []
    while n != 0:
        l_n.append(n % coding)
        n //= coding
    l_n = l_n[::-1]
    #print(l_n)
    numb = 0
    while i < len(l_n):
        numb += l_n[i] * 10**(len(l_n)-i-1)
        i += 1
    print(numb)

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
#1/2! + 1/3! + ... z dokładnoscia N cyfr dziesietnych (N jest rzedu 1000).
    N = 1000
    l_e = [0] * N
    i = 1
    e = 0
    l_e[0] = 1
    while i < N:
        l_e[i] = l_e[i-1] * 1/i
        i += 1
    for x in range(N):
        e += l_e[x]
        x += 1
    print(e)
    
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
    ciag_max = 50
    l_list = [0] * ciag_max
    i = 0
    x = 0
    l_sorted = []

    while temp != 0:
        temp = int(input("> "))
        if temp != 0:
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

if __name__ == "__main__":
    ex5()
