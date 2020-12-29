# Zadanie 31.
# Proszę napisać funkcję, która rozdziela listę na dwie listy.
# Pierwsza powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki
# na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja powinna zwrócić liczbę
# usuniętych elementów.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def divideList(dataL,evenPlus,oddMinus):
    d, e, o, = dataL, evenPlus, oddMinus

    prE = None
    while e != None:
        e, prE = e.next, e
    if e == None and prE == None:
        evenPlus = Node("!")
        prE = evenPlus
    
    prO = None
    while o != None:
        o, prO = o.next, o
    if o == None and prO == None:
        oddMinus = Node("!")
        prO = oddMinus
    
    cnt = 0
    while d != None:
        if d.val < 0 and d.val % 2 == 1:
            prO.next = Node(d.val)
            prO = prO.next
        elif d.val > 0 and d.val % 2 == 0:
            prE.next = Node(d.val)
            prE = prE.next
        else:
            cnt += 1
        d = d.next
    if evenPlus.val == "!":
        evenPlus = evenPlus.next
    if oddMinus.val == "!":
        oddMinus = oddMinus.next
    write(oddMinus)
    write(evenPlus)
    return cnt

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

z = Node(1)
z = pushBack(z,-3)
z = pushBack(z,-4)
z = pushBack(z,2)
z = pushBack(z,0)
z = pushBack(z,-1)
z = pushBack(z,8)

x = Node(6)
y = Node(-5)
print(divideList(z,x,y))