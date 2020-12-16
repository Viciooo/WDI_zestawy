def CntNum(n):
    tab = [0]*10
    while n!= 0:
        tab[n%10] += 1
        n //= 10
    return tab

print(CntNum(1101))