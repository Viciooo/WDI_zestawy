# Zadanie 24. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów przed cyklem.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def dlugosc_przed_cykl(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    cnt = 0
    p = first
    while p != q:
        p = p.next
        q = q.next
        cnt += 1
    return cnt

# def pushBack(first,n):
#     p, prev = first, None
#     while p != None:
#         p, prev = p.next, p
#     prev.next = Node(n)
#     return first

# def pushBackAddCycle(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     q = Node(n)
#     previous.next = q
#     q.next = first
#     return first

# z = Node(1)
# z = pushBack(z,3)
# z = pushBack(z,3)
# z = pushBackAddCycle(z,5)
# print(dlugosc_przed_cykl(z))

