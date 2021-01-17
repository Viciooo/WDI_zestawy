# - dane są dwa łańcuchy odsyłaczowe (listy) zawierające uporządkowane rosnąco, niepowtarzające się
# liczby naturalne. Napisz procedurę, która przyjmie za parametry wskaźniki do pierwszych elementów
# dwóch list i usunie z nich powtarzające się elementy. Np. mając dane listy (1, 2, 3, 7, 8, 15, 23) oraz
# (2, 5, 6, 8, 13, 20, 23) ma usunąć z obu elementy: 2, 8, 23 

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def doThings(f1,f2):
    tmp1 = Node("!",f1)
    tmp2 = Node("!",f2)
    p1, prev1, p2, prev2  = f1, tmp1, f2, tmp2

    while p1 != None and p2 != None:
        if p1.val == p2.val:
            prev1.next, p1 = p1.next, p1.next
            prev2.next, p2 = p2.next, p2.next
        elif p1.val < p2.val:
            p1, prev1 = p1.next, p1
        else:
            p2, prev2 = p2.next, p2

    write(tmp1.next)
    print("************")
    write(tmp2.next)

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

l1 = Node(1)
l1 = pushBack(l1,2)
l1 = pushBack(l1,3)
l1 = pushBack(l1,7)
l1 = pushBack(l1,8)
l1 = pushBack(l1,15)
l1 = pushBack(l1,23)
l2 = Node(2)
l2 = pushBack(l2,5)
l2 = pushBack(l2,6)
l2 = pushBack(l2,8)
l2 = pushBack(l2,13)
l2 = pushBack(l2,20)
l2 = pushBack(l2,23)

doThings(l1,l2)

# write(l1)
# print("************")
# write(l2)