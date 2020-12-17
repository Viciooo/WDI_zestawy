'''
1. Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000; int t[N][N];
Proszę napisać funkcję, która poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą
większą od 1, którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość
k. Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz,
kolumna) środka kwadratu. 
'''
N = 10

def func(t,k):
    size = 2
    while size < N:
        for r in range(N-size):
            for c in range(N-size):
                if t[r][c] * t[r][c+size] * t[r+size][c] * t[r+size][c+size] == k:
                    return (2*r+size)//2,(2*c+size)//2
        size += 2
    return False

t = [[1 for _ in range(N)]for _ in range(N)]
t[2][2] = 7
t[6][6] = 3
for i in t:
    print(i)
print(func(t,21))