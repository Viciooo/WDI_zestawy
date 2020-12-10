def waga_mb(T,k):
#mam sprawdzić czy da się odważyć n kg za pomocą odważników z tabeli T
#!!rozwiązanie maską bitową
    N =len(T)
    end = [1]*N
    mask = [0]*N
    while mask != end:
        suma = 0
        if mask[0] == 0:
            mask[0] = 1
            i = 1 
        elif mask[i] == 0:
            mask[i] = 1
            for j in range(i):
                mask[j] = 0
            i = 0
        else:
            i += 1
            continue
        for j in range(N):
            if mask[j] == 1:
                suma += T[j]
            if suma == k:
                print(mask)
                return True
    return False

def waga1(li,n,p):
    if n == 0: 
        return True
    if p == len(li):
        return False
    return waga1(li,n-li[p],p+1) or waga1(li,n,p+1) or waga1(li,n+li[p],p+1)

def waga(li,n,p=0,res=[]):
    if n == 0:
        print(res)
    if p == len(li):
        return None
    return waga(li,n-li[p],p+1,res+[li[p]]) or waga(li,n,p+1,res) or waga(li,n+li[p],p+1,res+[-li[p]])

def licz_pary(n,t):
    cnt = 0
    N = len(t)
    for i in range(N*N-1):
        for j in range(i+1,N*N):
            if t[i%N][i//N]*t[j%N][j//N] == n:
                cnt += 1
    return cnt

import random
def generuj(n):
    return [random.randint(1,9) for _ in range(n)]
    
def GenRnd2DmArr(N,start,end):
    from random import randint
    t = N*[0]
    for i in range(N):
        t[i] = N*[0]
    for j in range(N*N):
        t[j%N][j//N] = randint(start,end) 
    return t

def licz_nki(t,s,n,p=0,res=[]):
    global cnt
    if n == 1:
        for i in range(p,len(t)):
            if t[i] == s:
                res+=[t[i]]
                cnt += 1
                print(res)
    else:
        for i in range(p,len(t)):
            if s %t[i] == 0:
                licz_nki(t,s//t[i],n-1,i+1,res+[t[i]])

if __name__ == "__main__":
    cnt = 0
    t = generuj(20)
    print(t)
    licz_nki(t,24,3)
    print(cnt)

        
