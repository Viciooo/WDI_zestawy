# Zadanie 26. Proszę napisać funkcję, która sprawdza czy jedna lista 
# zawiera się w drugiej. Do funkcji należy przekazać wskazania na 
# pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def equal(p1,p2):
    while p1 != None:
        if p2 == None or p1.val != p2.val:
            return False
        p1, p2 = p1.next, p2.next
    return True

def ifBelongsToOther(f1,f2):
#sprawdza czy f1 zawiera się w f2
    while f2 != None:
        if equal(f1,f2):
            return True
        f2 = f2.next
    return False

# def pushBack(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     previous.next = Node(n)
#     return first

# def write(first):
#     while first != None:
#         print("[",first.val,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

# z = Node(1)
# z = pushBack(z,3)
# z = pushBack(z,1)
# z = pushBack(z,7)

# x = Node(1)
# x = pushBack(x,1)
# x = pushBack(x,4)
# x = pushBack(x,1)
# x = pushBack(x,3)
# x = pushBack(x,1)
# x = pushBack(x,2)

# print(ifBelongsToOther(z,x))

