def ex1():
#Zadanie 1. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch wyrazów ciagu Fibonacciego.    

    n = int(input("Podaj liczbę naturalną: "))
    a1 = 1
    a2 = 1

    while a2 < n**0.5:

        if n % a2 == 0:
            num = n // a2
            b1 = 1
            b2 = 1

            while b2 <= num:
                b2, b1 = b1 +b2, b2

                if num == b2:
                    return True

        a2, a1 = a1+a2, a2

    return False

def ex2():
#Zadanie 2. Napisac program wczytujacy trzy liczby naturalne a,b,n i wypisujacy rozwiniecie dziesietne
#ułamka a/b z dokładnoscia do n miejsc po kropce dziesietnej. (n jest rzedu 100)
    
    a = int(input('a ='))
    b = int(input('b ='))
    n = int(input('n ='))

    print(a//b, end='.')
    a = a%b
    for i in range(n):
        a *= 10
        print(a//b, end = '')
        a = a%b 


def ex3():
#Zadanie 3. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba naturalna jest palindromem, a nastepnie czy jest palindromem w systemie dwójkowym.    

    end = None
    liczba_pocz = int(input(">>>"))
    liczba = liczba_pocz
    rewers = 0

    #jeśli chcemy zmienić na sprawdzanie binarnego palindromu to trzeba
    #zamiast '10' używać '2' do dzielenia - tak samo w systemie '16-tkowym' itp 
    while liczba > 0:
        rewers = rewers*10 + liczba %10
        liczba //= 10
    end

    if liczba_pocz == rewers:
        print(True)
    else:
        print(False)
    end


def ex4():
#Zadanie 4. Liczba dwu-trzy-piatkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niz
#2,3,5. Jedynka tez jest taka liczba. Napisz program, który wylicza ile takich liczb znajduje sie w przedziale
#od 1 do N włacznie.   

    end = None

    n = int(input("n = "))

    counter = 0
    i2 = 1

    while i2 <= n:
        i3 = i2
        while i3 <= n:
            i5 = i3
            while i5 <= n:
                counter += 1
                i5 = i5 * 5
            end
            i3 = i3 * 3
        end
        i2 = i2 * 2
    end

    print(counter)


def factorize(n, factor):
  cnt = 0
  while n % factor == 0:
    n //= factor
    cnt += 1
  return cnt

def ex5():
#Zadanie 5. Dana jest liczba naturalna o niepowtarzajacych sie cyfrach posród których nie ma zera. Ile
#róznych liczb podzielnych np. przez 7 mozna otrzymac poprzez wykreslenie dowolnych cyfr w tej liczbie. Np.
#dla 2315 beda to 21, 35, 231, 315.
    n = int(input())
    mod = 7

    _n = n
    digits = 0
    while _n > 0:
        n = n*10 + _n%10
        _n //= 10
        digits += 1

    cnt = 0
    for i in range(1, 2**digits):
        candidate = 0
        _n = n

    while i > 0:
        if i % 2:
            candidate = candidate*10 + _n%10
            _n //= 10
            i //= 2
    print(candidate)

    if candidate % mod == 0:
        cnt += 1

    print(cnt)

def ex6():
#Zadanie 6. Napisac program wczytujacy liczbe naturalna z klawiatury i rozkładajacy ja na iloczyn 2 liczb
#o najmniejszej róznicy. Np. 30 = 5 * 6, 120 = 10 * 12.    

    n = int(input("Podaj liczbę naturalną: "))
    
    diff = n
    div = 2
    last_div = 0

    while n != 1:

        if div > n:
            div = 2

        if n % div == 0:
            n //= div
        
            if div - last_div < diff and last_div != 0:
                diff = div - last_div
                l1 = div
                l2 = last_div

            last_div = div

        div += 1

    print("l1*l2 = ", l1*l2, "l1 = ", l1, "l2 = ", l2)

def ex7():
#Zadanie 7. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba ta jest wielokrotnoscia dowolnego wyrazu ciagu danego wzorem An = n * n + n + 1.    

    x = int(input("Podaj liczbę naturalną: "))
    n = 1
    An = n * n + n + 1
    while An <= x:
        An = n * n + n + 1
    if x % An == 0:
        print(True)
    n += 1

def ex8():
#Zadanie 8. Pewnych liczb nie mozna przedstawic jako sumy elementów spójnych fragmentów ciagu Fibonacciego,
#np. 9,14,15,17,22. Prosze napisac program, który wczytuje liczbe naturalna n, wylicza i wypisuje
#nastepna taka liczbe wieksza od n. Mozna załozyc, ze 0 < n < 1000.    
    n = int(input("Pass n:"))
    while True:
        n += 1
        a, b = 1, 1
        suma = 1
        while suma < n:
            suma += b
            a, b = b, a+b
        a, b = 1, 1
        while suma > n:
            suma -= a
            a, b = b, a+b
        if suma != n:
            break 
    print(n)

def ex9():
#Zadanie 9. Napisac program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
#do k, metoda prostokatów.

    def f(x):
        return (1/x)
    a = 0#początek przedziału
    b = 10#koniec przedziału
    k = 0.001 #szerokość prostokąta
    x = a
    suma = 0
    while x < b:
        x += k
        suma += f(x)*k
    print(suma)

def ex10():
#Zadanie 10. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba ta jest wielokrotnoscia dowolnego wyrazu ciagu danego wzorem An = 3 * An−1 + 1, a pierwszy wyraz
#jest równy 2.
    n = int(input("Podaj liczbę: "))
    An = 2
    flaga = False
    while An < n:
        print(An)
        if n % An == 0:
            print("Jest")
            flaga = True #flaga logiczna - potrzebne jak się nie używa returnów bo to ma być program nie funkcja
            break
        An = 3*An + 1
    if flaga == False:
        print("Nie jest")

def ex11():    
#Zadanie 11. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#jej cyfry stanowia ciag rosnacy.
    n = int(input("n:"))
    rosnacy = True
    while n % 10 != 0:
        tmp = n%10
        n //= 10
        print(tmp,n%10)
        if tmp <= n%10: #w kolejności od tyłu ciąg musi być malejący
            rosnacy = False
            print("nierosnący")
            break
    if rosnacy == True:
        print("rosnący")

def ex12():
#Zadanie 12. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba ta zawiera cyfre równa liczbie swoich cyfr.
    n = int(input("n:"))
    cnt = 0
    tmp = n
    val = False
    while tmp != 0:
        cnt += 1
        tmp //= 10
    while n != 0:
        if n % 10 == cnt:
            print("Posiada")
            val = True
            break
        n //= 10
    if val == False:
        print("Nie posiada")

def ex13():
#Zadanie 13. Napisz program wczytujacy liczbe naturalna z klawiatury i odpowiadajacy na pytanie, czy
#liczba zakonczona jest unikalna cyfra.
    n = int(input("n:"))
    unikalna = True
    tmp = n%10
    n //= 10
    while n != 0:
        if n % 10 == tmp:
            unikalna = False
        n //= 10
    print(unikalna)

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

def IfHasXTimes1(x,t):
    cnt = 0
    for i in range(len(t)):
        if t[i] == 1:
            cnt += 1
            if cnt > x:
                return False
    if cnt == x:
        return True
    else:
        return False


def ex14():
#def ex14(): '''Kłopotliwe zadanko''' - można zrobić rekurencją albo maskami binarnymi/ trójkowymi
#Zadanie 14. Dane sa dwie liczby naturalne z których budujemy trzecia liczbe. W budowanej liczbie musza
#wystapic wszystkie cyfry wystepujace w liczbach wejsciowych. Wzajemna kolejnosc cyfr kazdej z liczb
#wejsciowych musi byc zachowana. Na przykład majac liczby 123 i 75 mozemy zbudowac liczby 12375, 17523,
#75123, 17253, itd. Prosze napisac funkcje która wyznaczy ile liczb pierwszych mozna zbudowac z dwóch
#zadanych liczb.
    n1 = 12
    n2 = 53 # miejsce występowania n2 oznaczam 1

    end = [0]*len(str(n1))
    length = len(str(n1)+str(n2))
    mask = [0]*length

    for i in range(len(str(n2))): #tworzę końcową odwróconą maskę binarną - odwróconą dlatego, żeby nie odwracać tej co powstanie
        end.append(1)
        
    while mask != end:
        if mask[0] == 0:
            mask[0] = 1
            i = 1 
        elif mask[i] == 0:
            mask[i] = 1
            for j in range(i):
                mask[j] = 0
            i = 0
        else:
            i += 1
            continue

        sNum = ""
        t_n1 = n1
        t_n2 = n2
        
        if IfHasXTimes1(len(str(n2)),mask) == True:
            for j in range(length):
                if mask[j] == 0:
                    sNum += str(t_n1 % 10)
                    t_n1 //= 10
                else:
                    sNum += str(t_n2 % 10)
                    t_n2 //= 10
                sNum = sNum[::-1]
            if IfPrime(int(sNum)) == True:
                print(sNum)    

def ex15():
#Zadanie 15. Napisac program znajdujacy wszystkie liczby N-cyfrowe dla których suma N-tych poteg cyfr
#liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3.
    N = 1
    cnt = 0
    while N < 1584: #max 9^3 +8^3 + 7^3
        suma = 0
        tmp = N
        while tmp != 0:
            suma += (tmp%10)**3
            tmp //= 10
        if suma == N:
            print(N)
            cnt += 1
        N += 1
    print("Jest ich:",cnt)

def DivList(n): #zwraca listę podzielników w postaci tablicy
    l = []
    tmp = n
    for i in range(2,n+1):
        if n % i == 0 and i != tmp:
            l.append(i)
        while n % i == 0:
            n //= i
    return l

def ex16(): #'''Przydałaby się optymalizacja'''
#Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb wystepujacych
#w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5*17, 8+5 = 5+1+7. Napisac program wypisujacy
#liczby Smitha mniejsze od 1000000.
    N = 1
    while N < 1000:
        l = DivList(N)
        sDiv = 0
        sN = 0
        tmp = N
        while tmp != 0:
            sN += tmp%10
            tmp //= 10
        for i in range(len(l)):
            while l[i] != 0:
                sDiv += l[i]%10
                l[i] //= 10
        if sN == sDiv:
            print(N)
        N += 1

def ex17():
#Zadanie 17. Napisac program wyliczajacy pierwiastek równania x^x = 2020 metoda stycznych.
    eps = 0.001
    x = 100
    while abs(x**x - 2020) > eps:
        x = (1/x)*((x-1)*x+(2020/(x**(x-1))))
        print(x)



def ex18():
#Zadanie 18. Mamy dane dwa ciagi A,B o nastepujacych zaleznosciach:
#A: a0 = 0, a1 = 1, an = an−1 − bn−1 * an−2
#B: b0 = 2, bn = bn−1 + 2 * an−1
#Prosze napisac program, który czyta liczby typu int ze standardowego wejscia i tak długo jak liczby te sa
#kolejnymi wyrazami ciagu An (tj. a0, a1, a2, ...) wypisuje na standardowe wyjscie wyrazy drugiego ciagu Bn
#(tj. b0, b1, b2, ...).

    cnt = 0
    An = 1
    Bn = 4
    tmp_1 = 1
    while True:
        n = int(input("n:"))
        if (n == 1 or n ==0) and cnt == 0:
            if n == 0:
                print(2)
                n = int(input("n:"))
            if n == 1:
                print(2)
                n = int(input("n:"))
            if n != 1:
                break
            print(4)
            cnt += 1
            continue
        if cnt == 1 or cnt == 0:
            while An != n:
                tmp_2 = An
                An =(Bn * tmp_1)*(-1) + tmp_2
                Bn = Bn + 2 * tmp_2
                tmp_1 = tmp_2
                cnt += 1

        else:
            tmp_2 = An
            An =(Bn * tmp_1)*(-1) + tmp_2
            Bn += 2 * tmp_2
            tmp_1 = tmp_2
            cnt += 2

        if n == An:
            print(Bn)
        else:
            break




        

def ex19():
#Zadanie 19. Napisac program wczytujacy dwie liczby naturalne a,b i wypisujacy rozwiniecie dziesietne
#ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)

    a = int(input("a: "))
    b = int(input("b: "))
    first_a = -1
    spaces = max(factorize(b, 2), factorize(b, 5))
    print(a//b, end='.')

    a %= b
    while True:
        cnt = 0
        while a < b:
            a *= 10
            cnt += 1

        if cnt > 1:
            print(0, end='')

        if a == first_a:
            break

        if spaces == 0:
            print('(', end='')
            first_a = a

        print(a//b, end='')
        a %= b
        spaces -= 1

    print(')')

def IfDigitsDiffer(num1,num2):
    for i in num1:
        for j in num2:
            if i == j:
                return False
    return True 

def ToDiffSystem(n,div):#zamienia liczbę na system o podstawie k
    l =[]
    while n > 0:
        tmp = n%div
        if tmp >=10:
            tmp = chr(55+tmp)
        l.append(str(tmp))
        n //=div
    l = l[::-1]
    return l  
    
def ex20():
#Zadanie 20. Dwie liczby naturalne sa rózno-cyfrowe jezeli nie posiadaja zadnej wspólnej cyfry. Prosze napisac
#program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
#2-16) w którym liczby sa rózno-cyfrowe. Program powinien wypisac znaleziona podstawe, jezeli podstawa
#taka nie istnieje nalezy wypisac komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzia jest
#podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11). 
    i = 2
    n1 = 332
    n2 = 572
    end = 0
    while i <= 16:
        l1 = ToDiffSystem(n1,i)
        l2 = ToDiffSystem(n2,i)    
        if IfDigitsDiffer(l1,l2) == True:
            end += 1
            print(i)
            break
        i += 1
    if end ==0:
        print("Brak takiego systemu")

if __name__ == "__main__":
    ex8()
    
