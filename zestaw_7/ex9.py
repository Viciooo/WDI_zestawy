# Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną.
# Kolejne elementy listy przechowują kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.

def addOneToLastEl(first):
    p, prev = first, None
    while p != None:
        p, prev = p.next, p 
    prev.val += 1
    return first

