# Zadanie 23. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self,val=None,idx=0,next=None):
        self.next = next
        self.val = val
        self.idx = idx

def getCycleLen(first): 
#jeśli zakładamy, że może to nie być cykl to dodajemy p != none
    p, prev = first.next, first
    while p.idx > prev.idx:
        p, prev = p.next, p
    return prev.idx - p.idx + 1

# def pushBack(first,n):
#     p, prev = first, None
#     while p != None:
#         p, prev = p.next, p
#     prev.next = Node(n,prev.idx+1)
#     return first

# def pushBackAddCycle(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     q = Node(n,previous.idx+1)
#     previous.next = q
#     q.next = first
#     return first

# z = Node(1)
# #z = pushBack(z,3)
# #z = pushBack(z,3)
# z = pushBackAddCycle(z,5)
# print(getCycleLen(z))

# def write(first):
#     while first != None:
#         print("[",first.val,first.idx,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

