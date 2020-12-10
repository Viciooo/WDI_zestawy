def pierwsza(a):
    if(a==2 or a==3):
        return True
    if(a<=1 or a%2==0 or a%3==0):
        return False
    i=6
    while(i<=a**(0.5)):
        if(a%(i-1)==0 or a%(i+1)==0):
            return False
        i+=6
    return True
print(pierwsza(4))


def ex1():
    a, b = 1, 1

    while a < 1_000_000:
        print(a)
        a, b = b, a+b
    ''' wersja beta
    a = 1
b = 0
temp = 0
while a < (10**6):
    print(a)
    temp = a
    a = a + b
    b = temp
    
    '''


def fib(a_in, b_in):
    curr_year = 2020
    a = a_in
    b = b_in
    while b < curr_year:
        a, b = b, a+b
        if b == curr_year:
            print(b_in, a_in)
            return True
    return False


def ex2():
    a = b = 1
    _sum = 2
    while True:
        for i in range(_sum // 3):
            a = i
            b = _sum - i
            if fib(a, b) or fib(b, a):
                exit()
        _sum += 1


def ex3():
    szukana_liczba = 16
# pierwszy ciąg
    a1 = 1
    a2 = 1
    suma = 0
# drugi ciąg
    b1 = 1
    b2 = 1
# 1 1 2 3 5 8 13 21 34 55 89
    while True:
        suma += a1
        if szukana_liczba == suma:
            print("tak")
            break
        if szukana_liczba < a1:
            print("nie ma takiego podciągu")
            break
    if szukana_liczba < suma:
            while True:
                if szukana_liczba == suma:
                    print(suma)
                    print("tak")
                    exit(0)
                if suma == 0:
                    break
                suma -= b1
                b1,b2 = b2,b1+b2
    a1, a2 = a2, a1+a2


def ex4():
    liczba = 8
    zliczanie = 0
    roznica = 1
    while liczba >= roznica:
        liczba-=roznica
        zliczanie+=1
        roznica+=2
    print(zliczanie)


def ex5():
    s = float(input())
    a = 1
    while abs(s - a*a) > 0.0001:
        a = 0.5*((s / a) + a)
    print(a)


def ex6():
    n = 2020
    eps = 0.000000001  # dokładność
    a = 0  # granica z lewej
    b = n  # granica z prawej
    # za każdym razem przecinam mój zbiór na pół
    # jeśli połowa do kwadratu większa od n to przecinam zbiór na pół
    # jeśli połowa do kwadratu mniejsza od n to wtedy połowa staje się początkiem zbioru
    while abs(b - a) > eps:
        c = (a + b) / 2  # połowa zbioru
        print(c)
         if c * c > n:
            b = c
         if c * c < n:
            a = c
         if c * c == n:
            a = b = c
    print(c)


def ex7():
    numb = int(input("Pass a number:"))
    a1, a2 = 1, 1
    while a1*a2 < numb:
        a1, a2 = a1+a2, a1
    if a1*a2 == numb:
        print("Yes")
    else:
        print("No")


def ex8():
    n = 31
    i = 2
    if n % i == 0 and n != 2:
        print("Parzysta inna od 2 nie jest pierwszą")
        exit(0)
    while i * i < n:
        if n % i == 0:
            break
        i += 1
    if i * i >= n:
        print("prime")
    else:
        print("not prime")


def ex9():
    numer = 27231
    dzielnik = 1
    while dzielnik != numer:
        if numer % dzielnik == 0:
            print(dzielnik, ",", end='')
        if dzielnik < numer:
            dzielnik += 1
    print(numer)


def ex10():
    numer = 4
    while numer < 10**6:
        suma = 0
        dzielnik = 1
        while dzielnik != numer:
            if numer % dzielnik == 0:
                suma += dzielnik
            if dzielnik < numer:
                dzielnik += 1
        if numer == suma:
            print(numer)
        numer += 1


def div_and_sum(_num,_sum):
    _div = 2
    while _div < _num:
        if _num % _div == 0:
            _sum += _div
        _div += 1

    return _sum


def ex11():
    i = 3
    temp = 0
    for i in range(10**6):
        suma_1 = 1
        suma_2 = 1
        suma_1 = div_and_sum(i,suma_1)
        suma_2 = div_and_sum(suma_1,suma_2) # suma dzielników sumy dzielników liczby i

        if suma_2 == i and suma_1 != suma_2 and temp != suma_1:
            print(suma_2,"    ", suma_1)
            temp = suma_2


def ex12():
    a = 321
    b = 441
    c = 660
    d = 1
    while (d <= a and d <= b and d <= c):
        if (a % d == 0 and b % d == 0 and c % d == 0):
            max = d
        d += 1
    print(max)

def ex13():
    a = 3  # liczba podawana
    b = 9  # liczba podawana
    c = 17 # liczba podawana
    nww = 1  # najmniejszy wspólny dzielnik
    d = 2  # dzielnik
    while a > 1:
        if d > a:
            d = 2
        if a % d == 0:
            a /= d
            nww *= d
            if b % d == 0:
                b /= d
            if c % d == 0:
                c /= d
        d += 1

    d = 2

    while b > 1:
        if d > b:
            d = 2
        if b % d == 0:
            b /= d
            nww *= d
            if c % d == 0:
                b /= d
        d += 1

    d = 2

    while c > 1:
        if d > c:
            d = 2
        if c % d == 0:
            c /= d
            nww *= d
        d += 1
    print(nww)


def ex14():
    x = input("Podaj wartość x dla cosx jako ułamek(bez pi): ")
    from math import pi
    y, z = 1, 1
    y = int(x[0])
    if len(x) >= 3:
        z = int(x[2])
    m = y/z
    cos = 1 - (1/2)*(m*pi)**2 + (1/24)*(m*pi)**4 - (1/720)*(m*pi)**6
    print(cos)


def ex15():
    from math import sqrt
    # x - dół równania pi = 2/x
    # start -
    x = sqrt(0.5)
    start = 2
    pierwiastek = sqrt(0.5)
    e = 0.00000000001
    while abs(start - x) >= e:
        temp = sqrt((0.5) + ((.5) * pierwiastek))
        start = x
        x *= temp
        pierwiastek = temp
    pi_value = 2.0 / x
    print(pi_value)


def ex16():
    counter = 0  # licznik kroków
    saver = 0  # miejsce gdzie zapisuje wyraz początkowy najdłuższej ilości kroków

    for x in range(2, 10000+1):
        a = x   #reset a
        temp_counter = 0 #reset licznika
        while a != 1:
            a = (a%2)*(3*a + 1) + (1-a%2) *(a/2)
            temp_counter += 1
        if temp_counter > counter:
            counter = temp_counter
            saver = x
    print("counter: ", counter)
    print("saver: ", saver)


def ex17():
    a1 = 2
    a2 = 5
    for x in range(100):
        iloraz = a1 / a2
        a2, a1 = a2 + a1, a2
        print(iloraz)


def ex18():
    s = float(input())
    a = 1
    temp = 1
    while abs(s - a*a*a) >= 0.0001:
        print(a)
        a = 0.33333333333*((s / a*a) + 2*a)
    print(a)


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)


def ex19():
    e = 0
    for x in range(100):
        e += 1/silnia(x)
    print(e)


def ex20():
    from math import sqrt
    a = 24
    b = 6
    for x in range(4):
        a, b = (a+b)/2, sqrt(a * b)
    print(a, "  ", b)


if __name__ == '__main__':
    ex3()
