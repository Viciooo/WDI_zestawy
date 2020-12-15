def cntEven(n):
    #liczy l.parzyste w sys 5
    if n <= 0:
        return False
    cnt = 0
    while n != 0:
        if (n % 5) % 2 == 0:
            cnt += 1
        n //=5
    return cnt

def otoczka(T,n,m):
    for _ in range(n-1):
        T.insert(0,[-1]*m)
        T.append([-1]*m)

    for i in range(m+2*n -2):
        for _ in range(n-1):
            T[i].insert(0,-1)
            T[i].append(-1)
    return T

def mainCourse(tab1,tab2):
    N = len(tab1)
    #tab2 > tab1
    tab2 = otoczka(tab2,N,len(tab2))
    M = len(tab2)
    for R in range(M-N):
        for C in range(M-N):
            cnt = 0
            for r in range(N):
                for c in range(N):
                    if tab2[r+R][c+C] != -1 and cntEven(tab1[r][c]) ==  cntEven(tab2[r+R][c+C]):
                        cnt += 1
            if cnt/N**2 >= 1/3:
                print(cnt)
                return True
    return False

t2=[[7,7,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
t1 = [[7,7,7],[0,0,0],[0,0,0]]
print(mainCourse(t1,t2))
#print(cntEven(-1))