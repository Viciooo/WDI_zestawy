# Zadanie 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne.
# W obu listach liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy
# liczby nie występujące w drugiej. Do funkcji należy przekazać wskazania na obie listy,
# funkcja powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def getLen(first):
    cnt = 0
    while first != None:
        cnt += 1
        first = first.next
    return cnt

def isIn(first,n):
    p = first
    while p != None and p.val < n:
        p = p.next
    if p == None or p.val > n:
        return False
    else:
        return True

def listDiff(f1,f2):
# tworzenie listy new jest zbędne ale proszono o usuwanie elemementów tak jakby lista miała być zwracana
#więc zamiast usuwać z tamtych list tworzę nową z el wspólnych - wydaje mi się to prostsze i szybsze
    new = Node("!")
    sumaDlList = getLen(f1) + getLen(f2)
    p = new
    newLen = 0
    while f1 != None:
        if isIn(f2,f1.val):
            p.next = Node(f1.val)
            newLen += 1
            p = p.next
        f1 = f1.next
    #write(new.next) 
    return sumaDlList - 2*newLen

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
# #x = pushBack(x,4)
# x = pushBack(x,3)
# #x = pushBack(x,7)

# print(listDiff(z,x))