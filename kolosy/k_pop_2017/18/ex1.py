''''Zadanie 1.
Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].

''''
def ex1(t):
    N = len(t)
    suma = 0
    m_len = -1
    for i in range(N-1):
        suma += t[i]
        j = i+1
        tmp = [0]
        k = 0
        while j < N:
            if tmp[k] == suma:
                tmp.append(0)
                k += 1
            tmp[k] += t[j]
            j += 1
        if len(tmp) > m_len:
            m_len = len(tmp) + 1
    return m_len


t =  [2,2,3,1,4,2,2,6,-2]
print(ex1(t))