'''1. Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
znalezionych i wypisanych sum.'''
def IfPrime(n):
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

def start(t1,t2):
    N = len(t1)
    cnt = 0
    def rek(t1,t2,N,i=0,suma=0):
        nonlocal cnt
        if i == N-1:
            if IfPrime(suma):
                print(suma)
                cnt += 1
            return False
        return rek(t1,t2,N,i+1,suma+t1[i])|rek(t1,t2,N,i+1,suma+t2[i])|rek(t1,t2,N,i+1,suma+t1[i]+t2[i])
    rek(t1,t2,N)
    print("********")
    return cnt

t1 = [1,3,2,4]
t2 = [9,7,4,8]
print(start(t1,t2))

#czas: 23 min z testami