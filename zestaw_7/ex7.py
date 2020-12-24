# Zadanie 7. Proszę napisać funkcję usuwającą ostatni element listy.
# Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def popBack(first):
    p = first
    l1,l2 = None, None
    while p != None:
        p, l1, l2 = p.next, p, l1
    l2.next = None
    return first
