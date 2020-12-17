'''Zadanie 2.
Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
maksymaln¡ liczb¦ par.'''

def programm(t1,t2):
    N = len(t1)
    maxi = -1
    def rec(cnt1=0,cnt2=0,s1=0,s2=0,i=0):
        nonlocal maxi,N
        if cnt1 == cnt2 and s1 == s2:
            if cnt1 > maxi:
                maxi = cnt1
        if i == N:
            return
        else:
            rec(cnt1+1,cnt2+1,s1+t1[i],s2+t2[i],i+1)
            rec(cnt1+1,cnt2,s1+t1[i],s2,i+1)
            rec(cnt1,cnt2+1,s1,s2+t2[i],i+1)
            rec(cnt1,cnt2,s1,s2,i+1)
    rec()
    return maxi

t1 = [1,2,3,4]
t2 = [5,1,2,3]
print(programm(t1,t2))

'''
t1 = [1,2,3,4]
t2 = [100,3,3,3]

def funk(t1,t2,li1=0,li2=0,suma1=0,suma2=0,cnt=0):

    if li1 == len(t1) or li2 == len(t2):
        if suma1 == suma2:
            return cnt
        return 0
    #wybieram oba
    cnt1 = funk(t1,t2,li1+1,li2+1,suma1+t1[li1],suma2+t2[li2],cnt+1)
    cnt2 = funk(t1,t2,li1+1,li2,suma1,suma2,cnt)
    cnt3 = funk(t1,t2,li1,li2+1,suma1,suma2,cnt)
    return max(cnt1,cnt2,cnt3)

print(funk(t1,t2))'''