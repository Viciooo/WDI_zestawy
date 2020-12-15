import math

def A(n):
    return n + 3
def B(n):
    return 2 * n
def C(n):
    m = math.floor(math.log10(n)+1)
    for _ in range(m):
        b = n // 10
        if (b%10) % 2 == 0 :
            n += 10
    return n
def check(x,y,n):
    cnt = 0
    def rek(x,y,n, result) :
        nonlocal cnt
        if n < 0 or x > y :
            return
        if x == y :
            cnt += 1
            print(result)
            return
        if result[-1] != 'A' :
            rek(A(x), y, n - 1, result + 'A')
        if result[-1] != 'B':
            rek(B(x), y, n - 1, result + 'B')
        if result[-1] != 'C':
            rek(C(x), y, n - 1, result + 'C')
    rek(A(x), y, n - 1, "A")
    rek(B(x), y, n - 1, "B")
    rek(C(x), y, n - 1, "C")
    return cnt

print(check(11,31,4))