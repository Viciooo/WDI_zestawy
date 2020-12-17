#Załóżmy, że Liczby są pierwsze w systemie 14 jeśli sklejenie kodu ascii części literowej
#z częścią nie literową daje liczbę pierwszą.
#Sprawdź czy da się utworzyć dwa równoliczne podzbioryu o zadanej sumie 
# składające się z liczb, które w ich reprezentacji 14'nastkowej są pierwsze

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 6
    while (i-1)**2<=n:
        if n %(i-1) == 0 or n%(i+1) == 0:
            return False
        i+=6
    return True
    
def ConvertToSys(n,sys):
    import math
    l = math.floor(math.log(n,sys)+1)
    number = 0
    dl = 0
    for _ in range(l):
        if n%sys < 10:
            number += (n%sys)*10**dl
        else:
            number += (n%sys + 55)*10**dl
            dl += 1
        dl += 1
        n //= sys
    return number

def start(t,k):
    n = len(t)
    for i in range(n):
        t[i] = ConvertToSys(t[i],14)
    def rek(cnt1=0,cnt2=0,s1=0,s2=0,i=0):
        nonlocal k,n,t
        if cnt1 == cnt2 and s1 + s2 == k:
            return True
        if i >= n:
            return False
        if is_prime(t[i]):
            return rek(cnt1+1,cnt2,s1+t[i],s2,i+1)or\
            rek(cnt1,cnt2+1,s1,s2+t[i],i+1)or\
            rek(cnt1,cnt2,s1,s2,i+1)
        else:
            return rek(cnt1,cnt2,s1,s2,i+1)
    return True if rek() else False



t = [2,3,3,2]
print(start(t,10))