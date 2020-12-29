# Zadanie 22. Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self,val=None,idx=0,next=None):
        self.next = next
        self.val = val
        self.idx = idx

def is_cycle(first):
    p, prev = first.next, first
    while p != None:
        if p.idx < prev.idx:
            return True
        p,prev = p.next,p
    return False

# def pushBack(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     previous.next = Node(n,previous.idx+1)
#     return first

# def pushBackAddCycle(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     q = Node(n,previous.idx+1)
#     previous.next = q
#     q.next = first
#     return first

# def write(first):
#     while first != None:
#         print("[",first.val,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

# z = Node(1)
# z = pushBack(z,3)
# z = pushBack(z,5)
# z = pushBack(z,7)
# z = pushBackAddCycle(z,2)

# print(is_cycle(z))
