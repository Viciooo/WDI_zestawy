def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2==0 or num%3==0:
        return False
    i = 6
    while (i-1)**2<=num:
        if num %(i-1) == 0:
            return False
        if num%(i+1) == 0:
            return False
        i+=6
    return True
def nwd(a,b):
    while b != 0:
        b,a = a%b,b
    return a
def silnia(nr):
    ret = 1
    for i in range(2,nr+1):
        ret *= i
    return ret
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def linearyzacja(t:list): #2 dim to 1 dim
    cop = []
    for i in t:
        for j in i:
            cop.append(j)
    return cop
#szachy start
#wieza
def wieza(tab,cop):
    #cop to krotka (row,column) tego czego szukam
    for i in tab:
        for j in tab:
            if (j[0] == cop[0] and j[1] == cop[1]):
                    continue
            if (j[0] == cop[0]) or (j[1] == cop[1]):
                return False
    return True
#hetman
def hetman(tab,cop):
    #cop to (row,column)
    for i in tab:
        for j in i:
            if (j[0] == cop[0] and j[1] == cop[1]):
                    continue
            if (j[0] == cop[0]) or (j[1] == cop[1]):
                return False
            x = abs(j[1]-cop[1])
            y = abs(j[0]-cop[0])
            if abs(x//y) == 1:
                return False
    return True
#kon
def kon(tab,x):
    #czy jest tak ze kon szachuje cos tam np ze to co pod koniem i suma jego szachownych jest rowna x
    i = 0
    while i <len(tab):
        j = 0
        while j<len(tab):
#            cop = (i,j)
            # prawo gora --^
            if i >= 1 and j <= len(tab)-3:
                pass
            #prawo dol --v
            if i <= len(tab)-2 and j <= len(tab)-3:
                pass
            #lewo gor --^
            if i >= 1 and j >= 2:
                pass
            #lewo dol --v
            if i<=len(tab)-3 and j>=2:
                pass
            #gora prawo ||>
            if i-2 >= 0 and j+1 <= len(tab)-1:
                pass
            #gora lewo ||<
            if i-2 >= 0 and j-1 >= 0:
                pass
            #dol prawo ||>
            if i+2 <= len(tab)-1 and j+1 <= len(tab)-1:
                pass
            #dol lewo ||<
            if i+2 <= len(tab)-1 and j-1 >= 0:
                pass
            j+=1
        i+=1
#krol na n ruchow
def krol(tab,krl,n):
    i = 0
    while i<len(tab):
        j =0
        while j<len(tab):
            k = i-n
            while k<=i+n:
                l = j-n
                while l<=j+n:
                    if k <0 or k >= len(tab):
                        break
                    if l<0:
                        continue
                    if l>= len(tab):
                        break
                    #end here is fucking git mimejsca gdzie krol zaszachuje w n ruchach to tab[k][l]
                    # i to kurwa kazdy a jak nie kadzy to wystarczy zamiast 2 pierwszych petli wzial i = krl[0] j = krl[1]
                    # i bd git cnie pzdr garek
                    l+=1
                k+=1
            j+=1
        i+=1

