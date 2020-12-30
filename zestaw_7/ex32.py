# Zadanie 32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są według rosnących potęg.
# Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane są przez wyżej opisane listy.
# Procedura powinna zwracać wskaźnik do nowo utworzonej listy reprezentującej wielomian wynikowy.
# Listy wejściowe powinny pozostać niezmienione.

class Node:
    def __init__(self,val=None,prev=None):
        self.val = val
        self.prev = prev

def pushFront(last,n):
    p,tmp = last, None
    while p != None:
        p, tmp = p.prev, p
    if p == None:
        tmp.prev = Node(n)
    else:
        p.prev = Node(n)
    return last

#polynomial - wielomian
def subtrPolynomial(l1,l2):
#l1 - lista 1 , l2 - lista 2
#od listy 1 odejmuje liste 2
    new = Node("!")
    while l1 != None and l2 != None:
        new = pushFront(new,l1.val-l2.val)
        l1, l2 = l1.prev, l2.prev
    if l1 != None:
        new = pushFront(new,l1.val)
        l1 = l1.prev
    elif l2 != None:
        new = pushFront(new,-l2.val)
        l2 = l2.prev
    return new.prev

z = Node(1)
z = pushFront(z,5)
z = pushFront(z,3)
z = pushFront(z,2)

x = Node(2)
x = pushFront(x,7)
x = pushFront(x,1)
# x = pushFront(x,2)

def writeWynik(last):
    cnt = 0
    while last!=None:
        wynik = ""
        if last.val < 0:
            wynik += str(last.val)
        else:
            wynik += "+" + str(last.val)
        if cnt > 0:
            wynik += "x^"+str(cnt)
        print(wynik,end=' ')
        last = last.prev
        cnt +=1

writeWynik(subtrPolynomial(z,x))