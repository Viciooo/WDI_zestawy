# Zadanie 25. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca wskaźnik do ostatniego elementu przed cyklem.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def lastEl(first):
    p, prev = first, None
    while p != None:
        if p.next == first:
            return p
        p, prev = p.next, p
    print("nie jest cyklem, ale ostatni el to: ",end ='')
    return prev #jeśli nie jest to cykl to zwróci ostatni element 

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def pushBackAddCycle(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    q = Node(n)
    previous.next = q
    q.next = first
    return first

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

z = Node(1)
z = pushBack(z,3)
z = pushBack(z,5)
z = pushBack(z,7)
#z = pushBackAddCycle(z,2)

print((lastEl(z)).val)
