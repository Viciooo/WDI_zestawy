# Zadanie 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne.
# W obu listach liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy
# liczby nie występujące w drugiej. Do funkcji należy przekazać wskazania na obie listy,
# funkcja powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def listDiff(f1,f2):
    #robię nową listę i dodaje tam wspolne elementy
    #do cnt zliczam ilość "przewinięć elementu mniejszego + to co ewentualnie zostanie w dłuższej z list"
    new = Node("!")
    p= new
    cnt = 0
    while f1 != None and f2 != None:
        if f1.val == f2.val:
            p.next = f1
            p = p.next
            f1, f2 = f1.next, f2.next
        else:
            cnt += 1
            if f1.val < f2.val:
                f1 = f1.next
            else:
                f2 = f2.next
        p.next = None
    while f1 != None:
        cnt += 1
        f1 = f1.next
    while f2 != None:
        cnt += 1
        f2 = f2.next
    print(cnt)
    return new.next

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

# z = Node(3)
# z = pushBack(z,2)
# z = pushBack(z,4)
# z = pushBack(z,8)

# x = Node(11)
# x = pushBack(x,8)
# x = pushBack(x,5)
# x = pushBack(x,7)

# write(listDiff(z,x))