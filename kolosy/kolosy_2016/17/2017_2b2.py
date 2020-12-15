'''Zadanie 2.
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
warto±¢ typu bool.'''

def func(t,A=0,B=0,a=0,b=0,i=0):
    if A == B != 0 and a == b:
        return True
    if i == len(t):
        return False
    func(t,A+t[i],B,a+1,b,i+1)or\
    func(t,A,B+t[i],a,b+1,i+1)or\
    func(t,A,B,a,b,i+1)