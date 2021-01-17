# Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną.
# Kolejne elementy listy przechowują kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.

class Node:
    def __init__(self,val=0,next=None):
        self.next = next 
        self.val = val

def addOneToLastEl(first):
    cp = first
    cp.val += 1
    while cp == 10 cp.next != None:
        cp.val = 0
        cp = cp.next
        cp.val += 1
    if cp.val == 10:
        cp.val = 0
        cp.next = Node(1)





