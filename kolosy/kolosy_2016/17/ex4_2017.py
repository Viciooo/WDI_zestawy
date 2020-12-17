'''Zadanie 2.
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
'''
def prime(x):
    if x in [2, 3, 5, 7]:
        return True
    return False

def rek(T, flag, p=1):
    if p == 9:
        print(T)
    for i in range(2, 10):
        if prime(i) and prime(T[p - 1]):
            continue
        if abs(T[p - 1] - i) < 2:
            continue
        if not flag[i - 1]:
            T[p] = i
            flag[i - 1] = True
            rek(T, flag, p+1)
            flag[i-1] = False
            
T = [0 for _ in range(9)]
T[0] = 1
flag = [False for _ in range(9)]
rek(T,flag)



#made by @Michał Wójcik ~ wzorcówka proszę Pana