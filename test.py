#Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Prosze napisac funkcje, która sprawdza czy mozna
#wybrac z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby zadne dwa wybrane
#elementy nie lezały w tej samej kolumnie ani wierszu. Do funkcji nalezy przekazac wyłacznie tablice oraz
#wartosc sumy, funkcja powinna zwrócic wartosc typu bool.

def Check(tab,n):
    for i in tab:
        if i == n:
            return False
    return True

def func(T,szukana,i=0,tw=[],tk=[]):
    if len(tw) > 0 and szukana == 0:
        return True
    if i == len(T)**2 or szukana < 0:
        return False
    if Check(tw,i%4) ==True and Check(tk,i//4) == True:
        return func(T,szukana-T[i%4][i//4],i+4-i//4,tw+[i%4],tk+[i//4]) or func(T,szukana,i+1,tw,tk)
    else:
        return func(T,szukana,i+1,tw,tk)

T = [[1,3,7,2],[1,3,7,2],[1,3,7,2],[1,3,7,2]]
print(func(T,4))
