# Zadanie 23. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def getCycleLen(first): 
#jeśli zakładamy, że może to nie być cykl to dodajemy p != none
    p = first.next
    cnt = 1
    while p != first:
        cnt += 1
        p = p.next
    return cnt

def pushBack(first,n):
    p, prev = first, None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(n)
    return first

def pushBackAddCycle(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    q = Node(n)
    previous.next = q
    q.next = first
    return first

z = Node(1)
z = pushBack(z,3)
z = pushBack(z,3)
z = pushBackAddCycle(z,5)
print(getCycleLen(z))

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

