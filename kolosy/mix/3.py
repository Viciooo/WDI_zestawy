'''1. Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000;
int t[N][N];
Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku
prawo-dół, liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić
informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.'''

n = 4
def programm(t):
    len_max = 2
    for x in range(1,n*n):
        r = x // n
        c = x % n
        i = 0
        while max(r,c)+i< n:
            a,b = t[r+i-1][c+i-1], t[r+i][c+i]
            if a < b: #rosnący
                q = b / a
                k = 0
                while max(r,c)+i+k+1 < n and t[r+i+k][c+i+k] * q == t[r+i+k+1][c+i+k+1]:
                    k += 1
                if k+2 > len_max:
                    len_max = k+2
            else:
                q = a / b
                k = 0
                while max(r,c)+i+k+1 < n and t[r+i+k][c+i+k] == t[r+i+k+1][c+i+k+1]* q:
                    k += 1
                if k+2 > len_max:
                    len_max = k+2
            i += 1
    return len_max if len_max > 2 else "ni ma takiego"

t = [[1,2,3,4],[9,6,7,8],[9,3,11,12],[13,14,3,16]]
for i in t:
    print(i)
print(programm(t))
