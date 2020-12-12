'''1. Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par'''

def nwd(n1,n2):
    i = 2
    if n2 > n1:
        n1, n2 = n2, n1
    while i <= n2:
        if n1 % i == 0 and n2 % i == 0:
            return False
        i +=1
    return True
def start(N):
    cnt = 0
    def func(N,A=0,i=0,B=0,j=0):
        nonlocal cnt
        if N == 0:
            if A != 0 and B != 0 and nwd(A,B):
                print(A,B)
                cnt += 1
            return
        return func(N//10,A+(N%10)*10**i,i+1,B,j) or func(N//10,A,i,B+(N%10)*10**j,j+1)
    func(N)
    return cnt//2
print(start(237))

#czas: zbyt długo bo jebałem się w 'optymalne rozwiązania'