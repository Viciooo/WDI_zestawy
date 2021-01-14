# Zadanie 25. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca wskaźnik do ostatniego elementu przed cyklem.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def lastEl(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    p, prev = p.next, p
    while p != q:
        p, prev = p.next, p
    return prev




