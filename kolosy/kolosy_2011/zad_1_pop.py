'''1. Mamy tablicę [1..max,1..max] of integer. Wyzeruj w niej wszystkie liczby które nie mają w tablicy innej
liczby, która powstałaby poprzez przestawienie jej cyfr. (uważając na 1000 i 0100 - nie dziala).
'''
def CntNum(n):
    tab = [0]*10
    while n!= 0:
        tab[n%10] += 1
        n //= 10
    return tab

def programm(t):
    N = len(t)
    tabOfTabs = [0]*N
    for i in range(N):
        tabOfTabs[i] = [0]*N
    for i in range(N*N):
        r = i // N
        c = i % N
        tabOfTabs[r][c] = CntNum(t[r][c])
    for j in range(N*N):
        for k in range(N*N):
            if tabOfTabs[k//N][k%N] == tabOfTabs[j//N][j%N] and k != j:
                print(j)
                break
        else:
            t[j//N][j%N] = 0
    return t

T = [[1,7,3],[1,2,3],[1,2,3]]#GenRnd2DmArr(4,1,10)
for i in T:
    print(i)
print("*********")
p = programm(T)

for i in p:
    print(i)
