'''1. Dana jest tablica typu tab1 = array [N,N] of integer wypełniona liczbami
naturalnymi. Proszę napisać procedurę, która wyznacza N największych wartości
występujących w tablicy, z których każde dwie są względnie pierwsze. Procedura powinna
sygnalizować brak możliwości wyznaczenia takich liczb.
'''
def relative(a, b):
    while b != 0:
        b, a = a % b, b
    if a == 1 :
        return True
    return False

def check(tab,N):
    for i in range(N):
        for j in range(N):
            if i != j and not relative(tab[i],tab[j]):
                return False
    return True

def start(T,N):
    mSuma = 0
    memory = []
    def rek(T,N,i=0,res=[]):
        nonlocal mSuma,memory
        if len(res) == N:
            if check(res,N):
                tmp = 0
                for i in range(N):
                    tmp += res[i]
                if tmp > mSuma:
                    mSuma = tmp
                    memory = res
            return False
        if i == N*N:
            return False
        rek(T,N,i+1,res+[T[i//N][i%N]])
        rek(T,N,i+1,res)
    rek(T,N)
    return memory
    
T = [[1,2,3],[2,2,2],[2,4,2]]
print(start(T,3))
