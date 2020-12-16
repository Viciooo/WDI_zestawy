'''1. Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
się co najmniej jeden element.'''

def cntEven(n):
    if n <= 0:
        return False
    cnt = 0
    while n != 0:
        if (n % 5) % 2 == 0:
            cnt += 1
        n //=5
    return cnt

def ex1(t1,t2):
    n1 = len(t1)
    n2 = len(t2)
    #n1 < n2
    for r1 in range(-n1+1,n2-n1+1):
        for c1 in range(-n1+1,n2-n1+1):
            pokryte, cnt = 0, 0
            for i in range(n1*n1):
                if i//n1 + r1 < 0 or i%n1 + c1 < 0:
                    continue
                else:
                    pokryte += 1
                    if cntEven(t1[i//n1][i%n1]) == cntEven(t2[i//n1+r1][i%n1+c1]):
                        cnt += 1
            if cnt != 0 and pokryte/cnt > 1/3:
                return True
    return False