'''Mamy tablicę tab[N][N] wypełnioną zerami i jedynkami, każdy wiersz reprezentuje liczbę zapisaną
binarnie. Liczby są tak duże że nie da się tego umieścić w typach podstawowych (int, long long).
Znaleźć najmniejszą/największą liczbę w tej tablicy.'''

'''def func(t,N):
    r_max = 0
    for r in range(1,N):
        for c in range(N):
            if t[r][c]>t[r_max][c]:
                r_max = r
                break
    return t[r_max]

t = [[0,1,0,1],[0,0,0,1],[0,1,1,1],[0,1,0,1]]
print(func(t,4))'''

'''Mamy tablicę tab[N][N] wypełnioną cyframi(0-9). Chcemy znaleźć największą/najmniejszą liczbę
utworzoną z 6 kolejnych cyfr leżących w jednym wierszu.'''

'''def fromTab(t,r,c):
    num = 0
    for i in range(c,c+6):
        num *= 10
        num += t[r][i]
    return num

def funk(t):
    n = len(t)
    num_max = 0
    for r in range(n):
        for c in range(n-5):
            tmp = fromTab(t,r,c)
            if tmp > num_max:
                num_max = tmp
    return num_max

t = [[2, 3, 4, 4, 5, 0, 6, 9, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 1, 2, 1, 1, 1, 6, 7, 8],
    [6, 4, 3, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]]

print(funk(t))'''