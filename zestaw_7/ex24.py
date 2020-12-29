# Zadanie 24. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów przed cyklem.

class Node:
    def __init__(self,val=None,idx=0,next=None):
        self.next = next
        self.val = val
        self.idx = idx

def getLenNoCycle(first): #długość przed cyklem
#jeśli zakładamy, że może to nie być cykl to dodajemy p != none
    p, prev = first.next, first
    while p.idx > prev.idx:
        p, prev = p.next, p
    return p.idx 

def pushBack(first,n):
    p, prev = first, None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(n,prev.idx+1)
    return first

def pushBackAddCycle(first,n):
    p, previous = first, None
    while p != None:
        if p.idx == 2:
            m = p
        p, previous = p.next, p
    q = Node(n,previous.idx + 1)
    previous.next = q
    q.next = m
    return first

def getCycleLen(first): 
#jeśli zakładamy, że może to nie być cykl to dodajemy p != none
    p, prev = first.next, first
    while p.idx > prev.idx:
        p, prev = p.next, p
    print(p.idx, prev.idx)
    return prev.idx - p.idx + 1

z = Node(1)
z = pushBack(z,3)
z = pushBack(z,3)
z = pushBack(z,3)
z = pushBackAddCycle(z,5)
print(getCycleLen(z))
print(getLenNoCycle(z))

def write(first):
    while first != None:
        print("[",first.val,first.idx,"] -----> ",end='',sep='')
        first = first.next
    print(None)

# write(z)