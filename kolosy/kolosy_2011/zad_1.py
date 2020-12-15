#Czy w jakimś systemie liczba tworzy podciąg max niemalejący o długości dokładanie 4

def ConvertTo(n,coding):
    l_n = []
    while n != 0:
        if n % coding < 10:
            l_n.append(n % coding)
        n //= coding
    l_n = l_n[::-1]
    return l_n

N = 286 #int(input())
for system in range(2,9):
    tab = ConvertTo(N,system)
    print(tab)
    i = 1
    m_cnt = 0
    while i < len(tab):
        if tab[i-1] <= tab[i]:
            cnt = 2
            i += 1
            while i < len(tab) and tab[i-1] <= tab[i]:
                cnt += 1
                i += 1
            if cnt > m_cnt:
                m_cnt = cnt
        i += 1
    if m_cnt == 4:
        print("Tak dla systemu",system,"i tab",tab)
        exit()

print("Nie :(")

