# Zadanie 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int,
# usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów.

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next
    
def utworz_linkliste_z_listy(T):
    if(len(T)==0):
        return None
    zbior=Node(T[0])
    kopia=zbior
    for k in T[1:]:
        nowy=Node(k)
        kopia.next=nowy
        kopia=kopia.next
    return zbior

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def f(zbior):
    if zbior is None or zbior.next is None:
        return zbior
    prev=zbior
    curr=zbior.next
    bufor=zbior.val
    while curr is not None:
        if(curr.val<bufor):
            bufor=curr.val
            prev.next, curr = curr.next, curr.next
        else:
            bufor=curr.val
            prev=curr
            curr=curr.next
    return zbior
        
zbior=utworz_linkliste_z_listy([5, 4, 4, 3, 5, 2, 1])
wypisz(f(zbior))