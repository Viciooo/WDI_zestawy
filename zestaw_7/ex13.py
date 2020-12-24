# Zadanie 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int,
# usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów.

class Node():
    def __init__(self,val=None):
        self.next = None
        self.val = val

# [1] -----> [5] -----> [1] -----> [3] -----> [7] -----> None
# **********
# [1] -----> [5] -----> [7] -----> None
# wynik funckji - podejrzewam że chodzi o coś innego

def func(first):
    p, prev = first.next, first
    while p != None:
        if prev.val > p.val:
            prev.next, p = p.next, p.next
        else:
            prev, p = p, p.next
    return first

def markThePray(first):
    wanted = Node("!")
    p, prev, q = first.next, first, wanted
    while p != None:
        if prev.val > p.val:
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

# [1] -----> [5] -----> [2] -----> [3] -----> [7] -----> None   - zbiór przed edytowaniem
# **********
# [2] -----> None   el.usuwany
# [1] -----> [5] -----> [3] -----> [7] -----> None  wynik