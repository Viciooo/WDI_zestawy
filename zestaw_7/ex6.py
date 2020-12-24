# Zadanie 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. 
# Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość.

class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def pushBack(first,n):
    p = first
    prev = None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(n)
    return first
