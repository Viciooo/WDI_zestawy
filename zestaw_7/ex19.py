# Zadanie 19. Elementy w liście są uporządkowane według wartości klucza.
# Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu.
# Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.

class Node():
    def __init__(self,val=None,next=None,prev=None):
        self.next = next
        self.prev = prev
        self.val = val

def popByVal(f,n):
    p = f
    while p != None and p.val <= n:
        if p.val == n:
            if p.prev == None:
                f = f.next
            elif p.next == None:
                p.prev.next = None
            else:
                p.prev.next = p.next
                p.next.prev = p.prev
        p = p.next
    return f

def uniq(first):
    p = first
    if p == None:
        return first
    p, pr = p.next, p
    while p != None:
        p = popByVal(p,pr.val)
        p, pr = p.next, p
    return first

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n,None,previous)
    return first

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

z = Node(1)
z = pushBack(z,1)
z = pushBack(z,1)
z = pushBack(z,2)
z = pushBack(z,3)
z = pushBack(z,3)
write(uniq(z))