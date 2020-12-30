# Zadanie 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list,
# według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową,
# która jest posortowana niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def sortByLastDigit(first):
    tab = [Node("!") for _ in range(10)]
    while first != None:
        tab[(first.val)%10] = pushBack(tab[(first.val)%10],first.val)
        first = first.next
    result = Node("!")
    for i in range(10):
        p = tab[i].next
        while p != None:
            result = pushBack(result,p.val)
            p = p.next
    return result.next


# def write(first):
#     while first != None:
#         print("[",first.val,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)


# z = Node(123)
# for i in range(20):
#     z = pushBack(z,i)
# write(z)
# write(sortByLastDigit(z))