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

def ex5():
#Zadanie 5. Dana jest liczba naturalna o niepowtarzajacych sie cyfrach posród których nie ma zera. Ile
#róznych liczb podzielnych np. przez 7 mozna otrzymac poprzez wykreslenie dowolnych cyfr w tej liczbie. Np.
#dla 2315 beda to 21, 35, 231, 315.

    n=int(input())
    licznik=0
    n2=n
    cyfry=1
    while n2//10!=0:
        cyfry+=1
        n2//=10
    mstart=2**cyfry-1
    wykladnik = cyfry - 1
    obrocona=0
    n2=n
    while (n2 % 10 != 0):

        obrocona = obrocona + (n2 % 10) * 10 ** wykladnik
        n2 //= 10
        wykladnik -= 1
    koncowa=0
    while(mstart!=0):
        m=mstart
        cyfry2=cyfry
        obrocona2=obrocona
        koncowa=0
        while cyfry2>=1:
            if(m>=2**(cyfry2-1)):
                m-=2**(cyfry2-1)
                koncowa=koncowa*10+obrocona2%10
                obrocona2//=10
            else:
                obrocona2//=10
            cyfry2-=1
        if(koncowa%7==0):
            licznik+=1
        mstart-=1
    print(licznik)

    '''n = int(input())
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

print(cnt)'''

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
    n1 = 123
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
    ex20()
    
