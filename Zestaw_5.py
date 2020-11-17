#Zadanie 1. Liczby wymierne sa reprezentowane przez krotke (l,m). Gdzie: l - liczba całkowita oznaczajaca
#licznik, m - liczba naturalna oznaczajaca mianownik. Prosze napisac podstawowe operacje na ułamkach,
#m.in. dodawanie, odejmowanie, mnozenie, dzielenie, potegowanie, skracanie, wypisywanie i wczytywanie.

def ReadFract():
    l = int(input("l:"))
    m = int(input("m:"))
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

def ShortenFract(t1):
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
    x1 = ShortenFract(x)
    y1 = ShortenFract(y)
    PrintFract(x1)
    PrintFract(y1)


if __name__ == "__main__":
    ex2()
