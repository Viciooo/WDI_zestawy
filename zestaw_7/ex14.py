# Zadanie 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int,
# usuwającą wszystkie elementy,których wartość dzieli bez reszty wartość bezpośrednio następujących po nich elementów.

class Node():
    def __init__(self,val=None):
        self.next = None
        self.val = val

def markThePray(first):
    wanted = Node("!")
    p, prev, q = first.next, first, wanted
    while p != None:
        if p.val % prev.val == 0:   #jedyna zmiana od poprzedniego zadania to ta linijka
            q.next = Node(p.val)
            q = q.next
        prev, p = p, p.next
    return wanted.next

def delete(space, n): 
    if space is None:
        return space
    prev = None
    curr = space
    if curr.val == n:
        curr = curr.next
        return curr
    while curr != None and curr.val != n:
        prev = curr
        curr = curr.next
    if curr is None:
        return space
    prev.next = curr.next
    return space

#? nie jestem pewny intepretacji tematu zadania