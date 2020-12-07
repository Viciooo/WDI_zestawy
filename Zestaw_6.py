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
cnt = 0
def ex11(il,T,nki,i=0):
    global cnt
    if i == len(T) or nki == 0:
        if il == 1 and nki == 0:
            cnt += 1
            return True
        else:
            return False
    if il % T[i] == 0:
        return ex11(il//T[i],T,nki-1,i+1)|ex11(il,T,nki,i+1)
    else:
        return ex11(il,T,nki,i+1)
    
#Zadanie 12. Prosze zmodyfikowac poprzedni program aby wypisywał znalezione n-ki.
repo=[]
def ex12(il,T,nki,i=0,res=[]):
    global repo
    if i == len(T) or nki == 0:
        if il == 1 and nki == 0:
            repo.append(res)
            return True
        else:
            return False
    if il % T[i] == 0:
        return ex12(il//T[i],T,nki-1,i+1,res+[T[i]])|ex12(il,T,nki,i+1,res)
    else:
        return ex12(il,T,nki,i+1,res)

#Zadanie 13. Napisac program wypisujacy wszystkie mozliwe podziały liczby naturalnej na sume składników.
#Na przykład dla liczby 4 sa to: 1+3, 1+1+2, 1+1+1+1, 2+2.
def wypisz(tab):
    for x in tab:
        if x != 0:
            print(x,end=" ")
        else:
            break
    print()

def ex13(t,i=0):
    if i <= len(t):
        while t[i] != 1 and t[i]>t[i+1]:
            t[i] -= 1
            t[i+1] += 1
            if t[i+1] <= t[i]:
                wypisz(t)
            ex13(t,i+1)


def start13(n):
    t = [0 for _ in range(n)]
    t[0] = n
    ex13(t)



#Zadanie 14. Problem wiez w Hanoi (tresc oczywista)
def hanoi(n,source,target,spare):
    global cnt
    if n > 0:
        cnt+=1
        hanoi(n-1,source,spare,target)
        target.append(source.pop())
        hanoi(n-1,spare,target,source)

#Zadanie 15. Problem 8 Hetmanów (tresc oczywista)


#Zadanie 16. Wyrazy budowane sa z liter a..z. Dwa wyrazy ”waza” tyle samo jezeli: maja te sama liczbe samogłosek
#oraz sumy kodów ascii liter z których sa zbudowane sa identyczne, na przykład "ula" -> 117, 108, 97
#oraz "exe" -> 101, 120, 101. Prosze napisac funkcje wyraz(s1,s2), która sprawdza czy jest mozliwe zbudowanie
#wyrazu z podzbioru liter zawartych w s2 wazacego tyle co wyraz s1. Dodatkowo funkcja powinna wypisac
#naleziony wyraz.
def weight(s):
    samogl = ['a','i','o','u','e','y']
    cnt = 0
    suma = 0
    for i in s:
        for j in samogl:
            if i == j:
                cnt += 1
                break
        suma += ord(i)
    return cnt,suma

def wyraz(s1,s2,i=1):
    if weight(s1)==weight(s2):
        print(s2)
        return True
    elif i == len(s1):
        return False
    else:
        return wyraz(s1,s2[:i-1]+s2[i:],i+1)|wyraz(s1,s2,i+1)

#Zadanie 17. Dane sa dwie liczby naturalne z których budujemy trzecia liczbe. W budowanej liczbie musza
#wystapic wszystkie cyfry wystepujace w liczbach wejsciowych. Wzajemna kolejnosc cyfr kazdej z liczb
#wejsciowych musi byc zachowana. Na przykład majac liczby 123 i 75 mozemy zbudowac liczby 12375, 17523,
#75123, 17253, itd. Prosze napisac funkcje która wyznaczy ile liczb pierwszych mozna zbudowac z dwóch
#zadanych liczb.

def getlen(n):
    c = 0
    while n != 0:
        n //= 10
        c +=1 
    return c

l1 = 0
l2 = 0
cnt = 0

def ex17(n1,n2,i=0,j=0,n3=0):
    global cnt,l1,l2
    if n1 == n2 == 0:
        if IfPrime(int(str(n3)[::-1])) == True:
            print(n3)
            cnt += 1
        return False
    if i > l1 or j > l2:
        return False
    if n1 != 0 or n2 !=0:
        return ex17(n1//10**(i+1),n2,i+1,j,n3+(n1%10**(i+1))*10**(i+j))|ex17(n1,n2//10**(j+1),i,j+1,n3+(n2%10**(j+1)*10**(j+i)))

def start17(n1,n2):
    global l1, l2
    l1 += getlen(n1)
    l2 += getlen(n2)
    ex17(n1,n2)
    
#Zadanie 18. W szachownicy o wymiarach 8x8 kazdemu z pól przypisano liczbe naturalna. Na ruchy króla
#nałozono dwa ograniczenia: król moze przesunac sie na jedno z 8 sasiednich pól jezeli ostatnia cyfra liczby na
#polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
#(np. naroznika) król nie moze wykonac ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
#T[8][8] wypełniona liczbami naturalnymi reprezentujaca szachownice. Lewy górny naroznik ma współrzedne
#w=0 i k=0. Prosze napisac funkcje sprawdzajaca czy król moze dostac sie z pola w,k do prawego dolnego
#naroznika.

def CanMove18(w,k,i):
    global m,T
    N = len(T)
    r = w+i[0]
    c = k+i[1]
    if r >= N or r < 0 or c >= N or c < 0:
        return False
    tmp = T[r][c]
    while tmp // 10 != 0:
        tmp //= 10
    if (T[w][k]%10) < tmp and max(7-k,7-w) >= max(7-c,7-r):
        return True

def KingMarch18(w=0,k=0):
    global T,m
    if w == k == len(T)-1:
        return "Marszruta udana"
    for i in m:
        if CanMove18(w,k,i) == True:
            x = KingMarch18(w+i[0],k+i[1])
            if x == "Marszruta udana":
                return "Marszruta udana"
    return "Koniec marszruty"

#Zadanie 19. Zadanie jak powyzej. Funkcja sprawdzajaca czy król moze dostac sie z pola w,k do któregokolwiek
#z narozników. #Zadanie 20. Zadanie jak powyzej. Funkcja powinna dostarczyc droge króla w postaci tablicy zawierajacej
#kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.
#2 zadania w 1
def CanMove19(w,k,i,R,C):
    global m,T
    N = len(T)
    r = w+i[0]
    c = k+i[1]
    if r >= N or r < 0 or c >= N or c < 0:
        return False
    tmp = T[r][c]
    while tmp // 10 != 0:
        tmp //= 10
    if (T[w][k]%10) < tmp and max(abs(C-k),abs(R-w)) >= max(abs(C-c),abs(R-r)):
        return True

def KingMarch19(w,k,R,C,res=[]):
    global T,m
    if w == k == len(T)-1:
        print(res)
        return True
    for i in m:
        if CanMove19(w,k,i,R,C) == True:
            x = KingMarch19(w+i[0],k+i[1],R,C,res+[i])
            if x == True:
                return True
    return False

#Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Prosze napisac funkcje, która sprawdza czy mozna
#wybrac z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby zadne dwa wybrane
#elementy nie lezały w tej samej kolumnie ani wierszu. Do funkcji nalezy przekazac wyłacznie tablice oraz
#wartosc sumy, funkcja powinna zwrócic wartosc typu bool.

if __name__ == "__main__":
    T = [[91 for _ in range(8)] for _ in range(8)]
    m = [(1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)] #moves
    print(KingMarch19(0,0,5,4))




