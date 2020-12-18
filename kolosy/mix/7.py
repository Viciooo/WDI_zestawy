'''1. Na szachownicy o wymiarach 201 wierszy i 201 kolumn umieszczamy 100 króli szachowych. Proszę
napisać program, który wczytuje z klawiatury położenia 100 króli (wiersz, kolumna), odnajduje dwa
króle jednakowo odległe od środka szachownicy i wypisuje ich pozycję (wiersz, kolumna). W
przypadku gdy żadna para króli nie spełnia warunku program kończy się stosownym komunikatem.
Odległość króla od środka to liczba jego ruchów, które musi wykonać aby dotrzeć do środka
szachownicy.'''

def func(t):
    n = 5
    tab = []
    for i in range(len(t)):
        d = max(abs(t[i][0]-(n+1)//2),abs(t[i][1]-(n+1)//2))
        for j in range(len(tab)):
            if tab != [] and tab[j][0] == d:
                return tab[j][1], t[i]
        tab.append((d,(t[i])))
    return "no nie ma"

t = [(0,0),(2,2),(4,4)]

print(func(t))


