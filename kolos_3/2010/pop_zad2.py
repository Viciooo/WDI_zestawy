def Count1(n):
    cnt = 0
    while n != 0:
        if n % 2 == 1:
            cnt += 1
        n //= 2
    return cnt

def recusion(tab,i=0,a=0,b=0,c=0):
    if i == len(tab):
        if a == b == c:
            return True
        return False
    return recusion(tab,i+1,a+Count1(tab[i]),b,c) or recusion(tab,i+1,a,b+Count1(tab[i]),c) or recusion(tab,i+1,a,b,c+Count1(tab[i]))

tab = [2,3,5,7,15,11]
print(recusion(tab))

