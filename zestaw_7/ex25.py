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

