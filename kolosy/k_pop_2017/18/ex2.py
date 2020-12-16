def programm(t1,t2):
    N = len(t1)
    maxi = -1
    def rec(t1,t2,cnt1=0,cnt2=0,s1=0,s2=0,i=0):
        nonlocal maxi,N
        if cnt1 == cnt2 and s1 == s2:
            if cnt1 > maxi:
                maxi = cnt1
        if i == N:
            return
        else:
            rec(t1,t2,cnt1+1,cnt2+1,s1+t1[i],s2+t2[i],i+1)
            rec(t1,t2,cnt1+1,cnt2,s1+t1[i],s2,i+1)
            rec(t1,t2,cnt1,cnt2+1,s1,s2+t2[i],i+1)
            rec(t1,t2,cnt1,cnt2,s1,s2,i+1)
    rec(t1,t2)
    return maxi

t1 = [1,2,3,4]
t2 = [5,1,2,3]
print(programm(t1,t2))