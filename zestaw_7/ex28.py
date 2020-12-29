# Zadanie 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) 
# liczby naturalne.W pierwszej liście liczby są posortowane rosnąco,
# a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby
# występujące w obu listach. Do funkcji należy przekazać wskazania na obie
# listy, funkcja powinna zwrócić łączną liczbę usuniętych elementów.


class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def is_in(first,n):
    p, prev =first, None
    while p != None and p.val < n:
        p, prev = p.next, p
    if p == None or p.val > n:
        return False
    if prev != None: #jeśli wartość nie jest na samym początku
        prev.next = p.next
        return first
    else: #jeśli wartość na samym początku
        return first.next
    
def deleteCommon(first_sorted,first_unsorted):
    p2, prev2 = first_unsorted, None
    cnt = 0
    while p2 != None:
        a = is_in(first_sorted,p2.val)
        if a != False:
            cnt += 2
            first_sorted = a
            if prev2 == None:
                first_unsorted, p2 = first_unsorted.next, p2.next
            else:
                prev2.next = p2.next
        else:
            p2, prev2 = p2.next, p2
    return cnt

# def write(first):
#     while first != None:
#         print("[",first.val,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

# def pushBack(first,n):
#     p, previous = first, None
#     while p != None:
#         p, previous = p.next, p
#     previous.next = Node(n)
#     return first

# z = Node(1)
# z = pushBack(z,2)
# z = pushBack(z,4)
# z = pushBack(z,8)

# x = Node(1)
# x = pushBack(x,4)
# x = pushBack(x,3)
# x = pushBack(x,7)

# print(deleteCommon(z,x))
