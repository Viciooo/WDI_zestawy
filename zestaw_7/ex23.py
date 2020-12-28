# Zadanie 23. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def countCycleLen(first):
    p, cnt = first, 0
    while p != None:
        cnt += 1
        if p.next == first:
            return cnt
        p = p.next
    return "to nie jest cykl :("
