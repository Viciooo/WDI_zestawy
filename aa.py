def check(t):
    suma = 0
    for i in range(13):
        #suma
        suma += abs((t[i][0] - t[i][1]) * (t[i][2]-t[i][3]))
        for j in range(i+1,13):
            #czy nachodza
            if t[j][0] > t[i][0] and t[j][0] < t[i][1] and ((t[j][2] > t[i][2] and t[j][2] < t[i][3]) or(t[j][3] > t[i][2] and t[j][3]<t[i][3])):
                return False
            elif t[j][1] > t[i][0] and t[j][1] < t[i][1] and ((t[j][2] > t[i][2] and t[j][2] < t[i][3]) or(t[j][3] > t[i][2] and t[j][3]<t[i][3])):
                return False
    if suma == 2012:
        return True
    return False

def reku(tab,pomc,index,idx_pom):
    if idx_pom == 13:
        return check(pomc)
    if index == len(tab):
        return False
    a = reku(tab,pomc,index+1,idx_pom)
    pomc[idx_pom] = tab[index]
    idx_pom+=1
    b = reku(tab,pomc,index+1,idx_pom)
    return a or b

def fun(tab):
    return reku(tab,[0 for _ in range(13)],0,0)