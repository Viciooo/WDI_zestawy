#Zadanie 1. Liczby wymierne sa reprezentowane przez krotke (l,m). Gdzie: l - liczba całkowita oznaczajaca
#licznik, m - liczba naturalna oznaczajaca mianownik. Prosze napisac podstawowe operacje na ułamkach,
#m.in. dodawanie, odejmowanie, mnozenie, dzielenie, potegowanie, skracanie, wypisywanie i wczytywanie.

def ReadFract():
    l = int(input("t[0]:"))
    m = int(input("t[1]:"))
    if m == 0:
        return "Błąd m == 0"
    tup = (l,m)
    return tup

def PrintFract(t1):
    print(t1[0],"/",t1[1],sep="")

def AddFract(t1,t2):
    if t1[1] == t2[1]:
        wynik = (t1[0]+t2[0],t1[1])
        return wynik
    else:
        wynik = (t1[0]*t2[1]+t2[0]*t1[1],t1[1]*t2[1])
        return wynik

def SubtrFract(t1,t2):
    if t1[1] == t2[1]:
        wynik = (t1[0]-t2[0],t1[1])
        return wynik
    else:
        wynik = (t1[0]*t2[1]-t2[0]*t1[1],t1[1]*t2[1])
        return wynik

def MultFract(t1,t2):

    wynik = (t1[0]*t2[0],t1[1]*t2[1])
    return wynik

def DivFract(t1,t2):
    wynik = (t1[0]*t2[1],t1[1]*t2[0])
    if wynik[0]<0 and wynik[1]<0:
        wynik1 = MultFract(wynik,(-1,-1))
        return wynik1
    return wynik

def FractToTheNPow(t1,n):
    lw = t1[0]**n
    mw = t1[1]**n
    wynik = (lw,mw)
    return wynik

def Sh(t1): #shorten fract
    lw = t1[0]
    mw = t1[1]
    i = 2
    while i <= lw:
        if lw % i == 0 and mw % i == 0:
            lw //= i
            mw //= i
        else:
            i += 1
    wynik = (lw,mw)
    return wynik

def ex2():
#Zadanie 2. Uzywajac funkcji z poprzedniego zadania prosze napisac funkcje rozwiazujaca układ 2 równan
#o 2 niewiadomych.
    print("Podaj arg równania tego typu: ax + by = w i cx + dy = v")
    a = (1,1)   #ReadFract()
    b = (2,1)   #ReadFract()
    w = (7,1)   #ReadFract()
    c = (2,1)   #ReadFract()
    d = (-1,1)   #ReadFract()
    v = (1,1)   #ReadFract()

    b0 = MultFract(b,(-1,1))
    b1 = DivFract(b0,a)
    w1 = DivFract(w,a)
    d0 = MultFract(d,(-1,1))
    d1 = DivFract(d0,c)
    v1 = DivFract(v,c)
    diff_y = SubtrFract(b1,d1)
    diff_wv = SubtrFract(v1,w1)
    y = DivFract(diff_wv,diff_y)
    x = AddFract(MultFract(d1,y),v1)
    x1 = Sh(x)
    y1 = Sh(y)
    PrintFract(x1)
    PrintFract(y1)

def ex3(t):
#Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Połozenie
#hetmanów jest opisywane przez tablice dane = [(w1, k1), (w2, k2), (w3, k3), ...(wN, kN)] Prosze napisac funkcje,
#która odpowiada na pytanie: czy zadne z dwa hetmany sie nie szachuja? Do funkcji nalezy przekazac
#połozenie hetmanów.
    N = len(t)
    M = 100
    tab = [0]*M
    r = 0
    c = 0
    for i in range(M):
        tab[i]=[0]*M
    for j in range(N):
        q = t[j] #qween
        for r in range(M):
            if tab[r][q[1]] == -1:
                return False
            tab[r][q[1]] = 1
        for c in range(M):
            if tab[q[0]][c] == -1:
                return False
            tab[q[0]][c] = 1

        r, c = q[0], q[1]
        while r >= 0 and c >= 0:
            if tab[r][c] == -1:
                return False
            tab[r][c] = 1
            r-=1
            c-=1

        r, c = q[0], q[1]
        while r >= 0 and c < M:
            if tab[r][c] == -1:
                return False
            tab[r][c] = 1
            r-=1
            c+=1

        r, c = q[0], q[1]
        while r < M and c < M:
            if tab[r][c] == -1:
                return False
            tab[r][c] = 1
            r+=1
            c+=1

        r, c = q[0], q[1]
        while r < M and c >= 0:
            if tab[r][c] == -1:
                return False
            tab[r][c] = 1
            r+=1
            c-=1

        tab[q[0]][q[1]] = -1

    Print2DmTab(tab)
    return True

def ex4(t):
#Zadanie 4. Dana jest tablica zawierajaca liczby wymierne. Prosze napisac funkcje, która policzy wystepujace
#w tablicy ciagi arytmetyczne (LA) i geometryczne (LG) o długosci wiekszej niz 2. Funkcja powinna
#zwrócic wartosc 1 gdy LA > LG, wartosc -1 gdy LA < LG oraz 0 gdy LA = LG.
    N = len(t)
    LG = 2
    LA = 2
    for i in range(1,N):
        cg = 2
        ca = 2
        q = Sh(DivFract(t[i],t[i-1]))
        r = SubtrFract(t[i],t[i-1])
        print(r)

        j = i
        while j+1 < N and Sh(MultFract(t[j],q))==Sh(t[j+1]):
            PrintFract(t[j])
            PrintFract(t[j+1])
            cg += 1
            j += 1
        if cg > LG:
            LG = cg

        j = i
        while j+1 < N and Sh(AddFract(t[j],r))==Sh(t[j+1]): #sprawdzanie LA
            ca += 1
            j += 1
        if ca > LA:
            LA = ca
    if LA == LG:
        print(LA)
        return 0
    elif LA > LG:
        print(LA,LG)
        return 1
    else:
        print(LG,LA)
        return -1
    
def ex5(t):
#Zadanie 5. Dany jest zbiór punktów lezacych na płaszczyznie opisany przy pomocy struktury dane =
#[(x1, y1), (x2, y2), (x3, y3), ...(xN, yN)] Prosze napisac funkcje, która zwraca wartosc True jezeli zbiorze istnieja
#4 punkty wyznaczajace kwadrat o bokach równoległych do osi układu współrzednych, a wewnatrz
#tego kwadratu nie ma zadnych innych punktów. Do funkcji nalezy przekazac strukture opisujaca połozenie
#punktów.
    N = len(t)
    s = 0
    while N-s >= 4:
        for i in range(s,N):
            points = 0
            a = t[i][0]
            b = t[i][1]
            cnt = 1
            if a == b:
                continue
            for j in range(N):
                if t[j] == (b,a):
                    cnt += 1
                    for k in range(N):
                        if t[k] == (a,a):
                            cnt += 1
                            for l in range(N):
                                if t[l] == (b,b):
                                    cnt += 1
            if cnt == 4:
                if a > b:
                    sup = a
                    inf = b
                else:
                    sup = b
                    inf = a
                for h in range(N):
                    if t[h][0] > t[h][1]:
                        s1 = t[h][0]
                        i1 = t[h][1]
                    else:
                        s1 = t[h][1]
                        i1 = t[h][0]
                    if s1 <= sup and i1 >= inf:
                        points += 1
                if points == 4:
                    return True
                    
        s += 1
    return False

def cAdd(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def cSubtr(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1])

def cMulti(t1,t2):
    return (t1[0]*t2[0]-(t1[1]*t2[1]),t1[0]*t2[1]+t1[1]*t2[0])

def cDiv(t1,t2):
    w = cMulti(t1,(t2[0],-t2[1]))
    v = cMulti(t2,(t2[0],-t2[1]))
    return (w[0]/v[0],w[1]/v[0])

def cToPow(t,n):
    if n == 0:
        return (1,0)
    re = t[0]
    im = t[1]
    tab = [t[0],t[1]]
    for _ in range(1,n):
        tmp = cMulti((tab[0],tab[1]),(re,im))
        tab[0] = tmp[0]
        tab[1] = tmp[1]
        del tmp
    tmp = (tab[0],tab[1])
    return tmp

def cPrint(t):
    print(t[0]," + (",t[1],"i)",sep='')

def cRead():
    re = int(input("re:"))
    im = int(input("im:"))
    return (re,im)

#def cSqrt(t):
#    x_

#Zadanie 6. Liczby zespolone sa reprezentowane przez krotke (re, im). Gdzie: re - czesc rzeczywista liczby,
#im - czesc urojona liczby. Prosze napisac podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
#odejmowanie, mnozenie, dzielenie, potegowanie, wypisywanie i wczytywanie.

def ex7(a,b,c):
#Zadanie 7. Uzywajac funkcji z poprzedniego zadania prosze napisac funkcje rozwiazujaca równanie kwadratowe
#o współczynnikach zespolonych.
    #równanie postaci x^2*a + bx +c = 0
    delta = cSubtr(cToPow(b,2),cMulti((4,0),cMulti(a,c)))
    if delta[0] < 0 and delta[1] == 0:
        p_delta = (0,(delta[0]*(-1))**0.5)
    elif delta[0] >= 0 and delta[1] == 0:
        p_delta = ((delta[0])**0.5,0)
    else:
        p_delta = ((((delta[0]+(delta[0]**2+delta[1]**2)**0.5)/2)**0.5),0)


    x1 = cDiv(cAdd(cMulti(b,(-1,0)),p_delta),cMulti(a,(2,0)))
    x2 = cDiv(cSubtr(cMulti(b,(-1,0)),p_delta),cMulti(a,(2,0)))
    cPrint(x1)
    if x1 != x2:
        cPrint(x2)

def Print2DmTab(t):
    for i in range(len(t)):
        print(t[i])

if __name__ == "__main__":
    #t = [(1,1),(5,1),(1,5),(5,5),(10,1)]
    #cPrint((2,-3))
    ex7((1,3),(1,-2),(5,3))
