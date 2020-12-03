# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
import math

# 2178 % 100 78 // 1000 2 * 10^i


def prime_test(num):
    if (num % 2 == 0 and num != 2) or num <= 9:
        return False
    i = 3
    while i <= num**(1/2):
        if num % i == 0:
            return False
        i += 2
    return True

dictionary = {}

def funkcja(num):
    global dictionary
    if num <= 10:
        return False
    for i in range(0, math.floor(math.log10(num)) + 1):
        right_side = num % 10**i
        left_side = num // 10**(i+1)
        num2 = left_side * 10**i + right_side
        if prime_test(num2):
            dictionary[num2] = True
        funkcja(num2)
    return None

#Zadanie 2. ”Waga” liczby jest okreslona jako ilosc róznych czynników pierwszych liczby. Na przykład
#waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierajaca liczby
#naturalne. Prosze napisac funkcje, która sprawdza czy mozna elementy tablicy podzielic na 3 podzbiory o
#równych wagach. Do funkcji nalezy przekazac wyłacznie tablice, funkcja powinna zwrócic wartosc typu Bool.

def waga(n):
    i = 2
    cnt = 0
    while n != 1:
        if n % i == 0:
            while n % i == 0:
                n //= i
            cnt += 1
        i += 1
    return cnt

def ex2(T,p1=0,p2=0,p3=0):
    if len(T) == 0:
        return p1 == p2 == p3
    return ex2(T[1:],p1+waga(T[0]),p2,p3) or ex2(T[1:],p1,p2+waga(T[0]),p3) or ex2(T[1:],p1,p2,p3+waga(T[0]))

l = [2*3*5,3*7*11,7*11*13,7]


#Zadanie 3. Szachownica jest reprezentowana przez tablice T[8][8] wypełniona liczbami naturalnymi zawierajacymi
#koszt przebywania na danym polu szachownicy. Król szachowy znajduje sie w wierszu 0 i kolumnie
#k. Król musi w dokładnie 7 ruchach dotrzec do wiersza 7. Prosze napisac funkcje, która wyznaczy minimalny
#koszt przejscia króla. Do funkcji nalezy przekazac tablice t oraz startowa kolumne k. Koszt przebywania na
#polu startowym i ostatnim takze wliczamy do kosztu przejscia.

def King(t,k,r=0,suma=0,res=[],end=0):
    if r == 0:
        suma += t[r][k]
    if r == len(t)-1:
        res.append(suma)
        if end == len(t) - 1:
            return min(res)
        return 0
    if k+1 == len(t):
        return King(t,k-1,r+1,suma+t[r+1][k-1]) or King(t,k,r+1,suma+t[r+1][k],res,end+1) 
    elif k == 0:
        return King(t,k+1,r+1,suma+t[r+1][k+1]) or King(t,k,r+1,suma+t[r+1][k],res,end+1)
    else:
        return King(t,k+1,r+1,suma+t[r+1][k+1]) or King(t,k-1,r+1,suma+t[r+1][k-1]) or King(t,k,r+1,suma+t[r+1][k],res,end+1)

def GenRnd2DmArr(N,start,end):
    from random import randint
    t = N*[0]
    for i in range(N):
        t[i] = N*[0]
    for j in range(N*N):
        t[j%N][j//N] = randint(start,end) 
    return t

#Zadanie 4. Problem skoczka szachowego. Prosze napisac funkcje, która wypełnia pola szachownicy o
#wymiarach NxN ruchem skoczka szachowego.

def horse(T,n,r,c,dim):
    ruchy=((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
    if dim == 0:
        return True
    if r >=0 and r < n and c >= 0 and c < n and T[r][c] == 0:
        T[r][c] = 1
        for i in range(8):
            a = horse(T,n,ruchy[i][0]+r,ruchy[i][1]+c,dim-1)
            if a:
                return a
        T[r][c] = 0
        return a 
    return False

def ex4(n):
    T = [0]*n
    for i in range(n):
        T[i] = [0]*n
    for r in range((len(T)+1)//2):
        for c in range(r,(len(T)+1)//2):
            if horse(T,n,r,c,n**2) == True:
                return True
    return False

#Zadanie 5. Dany jest ciag zer i jedynek zapisany w tablicy T[N]. Prosze napisac funkcje, która odpowiada
#na pytanie czy jest mozliwe pociecie ciagu na kawałki z których kazdy reprezentuje liczbe pierwsza. Długosc
#kazdego z kawałków nie moze przekraczac 30. Na przykład dla ciagu 111011 jest to mozliwe, a dla ciagu
#110100 nie jest mozliwe.

def binToDec(binary):
    decimal, i= 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

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

def ex5(T, p=2, s=0, w=False):
    if p > len(T):
        return False
    if w == True:
        b = '' #binary
        for i in range(s,len(T)):
            b += str(T[i])
        if len(b) == 0:
            return True
        k = 0
        while k < len(b) and b[k] == '0':
            b = b[:k] + b[(k+1):]
        if len(b) == 0:
            return False
        if len(T) - p <= 30 and IfPrime(binToDec(int(b))) == True :
            return True
        else:
            return ex5(T,p+2,p,True) or ex5(T,p+1,s)
    else:
        b = '' 
        for i in range(s,p):
            b += str(T[i])
        if IfPrime(binToDec(int(b))) == True:
            return ex5(T,p+2,p,True) or ex5(T,p+1,s)
        else:
            return ex5(T,p+1,s)

#Zadanie 6. Dana jest tablica T[N]. Prosze napisac funkcje, która znajdzie niepusty, najmniejszy (w sensie
#liczebnosci) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
#Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic sume elementów znalezionego podzbioru.
#Na przykład dla tablicy: [1,7,3,5,11,2] rozwiazaniem jest liczba 10 i 8.
def ex6(T,i=0,Suma=0,iSuma=0,l=0,mini=1000,mSuma=0):
    if i+1 > len(T):
        if Suma == iSuma != 0:
            if l < mini:
                mini = l
                mSuma = Suma
        return mini, mSuma
    a = ex6(T,i+1,Suma+T[i],iSuma+i,l+1,mini,mSuma)
    if a[0] < mini:
        mini = a[0]
        mSuma = a[1]
    a = ex6(T,i+1,Suma,iSuma,l,mini,mSuma)
    if a[0] < mini:
        mini = a[0]
        mSuma = a[1]
    return mini,mSuma
#zad7,8,9
def waga8(li,n,p,t=[]):
    if n ==0:
        print(t)
        return True
    if p == len(li):
        return False
    return waga8(li,n-li[p],p+1,t+[li[p]]) or waga8(li,n,p+1,t) or waga8(li,n+li[p],p+1,t+[-li[p]])

#Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (tresc oczywista)
def sub_matrix(matrix, i, j):
    matrix_del = []
    for row in (matrix[:i] + matrix[i + 1:]):
        matrix_del.append(row[:j] + row[j + 1:])
    return matrix_del

def det(matrix):
    # wyznacznik dla macierzy 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    sum_ = 0
    # przechodzimy przez kolejne kolumny (wiersz zerowy)
    for column in range(len(matrix)):
        sign = (-1)**column
        sub_matrix_det = det(sub_matrix(matrix, 0, column))
        sum_ += sign * matrix[0][column] * sub_matrix_det
    # myślę, że to jest jasne, proszę sobie to jeszcze przemyśleć
    # Kubuś <3
    return sum_

#Zadanie 11. Dana jest tablica T[N]. Prosze napisac program zliczajacy liczbe “enek” o okreslonym iloczynie.
def ex11(il,T,nki,i=0,res=[]):
    print(res)
    if i == len(T)-1 or nki == 0:
        if il == 1:
            print(res)
            return True
        else:
            return False
    if il % T[i] == 0:
        return ex11(il//T[i],T,nki-1,i+1,res+[T[i]])|ex11(il,T,nki,i+1,res)
    else:
        return ex11(il,T,nki,i+1,res)

if __name__ == "__main__": 
    print(ex4(6))

