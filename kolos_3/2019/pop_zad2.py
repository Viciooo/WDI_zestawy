# 2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
# się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
# klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
# napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
# Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
# najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]
# Dane opisujące zestaw:
# const int N= …
# struct klocek {
#  int a;
#  int b; // b>a
# };
# klocek zestaw[N];
# Do funkcji należy przekazać zestaw klocków, funkcja powinna zwrócić największą długość ciągu jaki można z tego
# zestawu zbudować. Wskazówka : kiedy z zestawu klocków da się zbudować ciąg?
def start(zestaw):
    n = len(zestaw)
    mCnt = 0
    maxi = []
    def rec(zestaw, last, cnt=0, i=0, res=[]):
        nonlocal mCnt, maxi
        if i == n:
            if cnt > mCnt:
                mCnt = cnt
                maxi = res
            return
        if last == zestaw[i][0]:
            rec(zestaw,zestaw[i][1],cnt+1,i+1,res+[zestaw[i]])
        if last == zestaw[i][1]:
            rec(zestaw,zestaw[i][0],cnt+1,i+1,res+[(zestaw[i][1],zestaw[i][0])])
        else:
            rec(zestaw,last,cnt,i+1,res)
    for x in range(n):
        rec(zestaw,zestaw[x][0])
        rec(zestaw,zestaw[x][1])
    print(maxi)
    return mCnt

zestaw = [(2,8), (0,1), (2,3), (3,6), (2,6), (2,9), (3,4), (6,7)]

print(start(zestaw))