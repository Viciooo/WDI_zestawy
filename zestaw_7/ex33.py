# Zadanie 33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
# Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐ 
# └───────────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady poprzedzania.
# Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
# czy udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def ifCan(s1,s2):
    return ord(s1[-1]) < ord(s2[0])

def insert(p,s):
#próbuje wcisnąć do listy string o val = s
    if p == None: #lista pusta
        print("True")
        return Node(s)

    curr, prev, q = p.next, p, Node(s)

    if curr == None: #lista ma jeden element
        if ifCan(prev.val,s):
            prev.next, q.next = q, prev
            print("True")
            return q
        else:
            print("False")
            return p

    #jeśli dodaje "na koniec cyklu"
    if ifCan(prev.val,s) and ifCan(s,curr.val):
        prev.next, q.next = q, curr
        print("True")
        return q

    while curr != p:
        if ifCan(prev.val,s) and ifCan(s,curr.val):
            prev.next, q.next = q, curr
            print("True")
            return q
        curr, prev = curr.next, curr

    print("False")
    return p

def writeCycle(first):
    p, prev = first.next, first
    while p != first:
        print("[",prev.val,"] -----> ",end='',sep='')
        p, prev = p.next, p

    print("[",prev.val,"] -----> ")

z = None
z = insert(z,"zosia")
z = insert(z,"bartek")
z = insert(z,"leszek")
z = insert(z,"marek")
z = insert(z,"ola")
z = insert(z,"zala_makota_d")
z = insert(z,"aa")
writeCycle(z)
print(ord("k"),ord("m"))




