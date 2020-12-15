'''2. Napisz procedurę, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie co najmniej
dwucyfrowe liczby pierwsze, powstale poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
'''

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

def start(n):
    import math
    l = math.floor(math.log10(n)+1)
    res = []
    tmp = l
    def rek(n,l):
        nonlocal res
        if l == 1:
            return
        if IfPrime(n):
            if n not in res:
                res.append(n)
        for i in range(1,l+1):
            rek((n//(10**i))*10**(i-1)+n%10**(i-1),l-1)
    rek(n,l)
    for el in res:
        if el != n:
            print(el)

start(121453)

