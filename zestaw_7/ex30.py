# Zadanie 30. 
# Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy.
# Elementy w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej
# kolejności. Proszę napisać funkcję, która z dwóch takich list stworzy jedną,
# w której uporządkowane elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić wskazanie
# na listę wynikową. 
# Na przykład dla list: 2 -> 3 -> 5 ->7-> 11 | 8 -> 2 -> 7 -> 4 
# powinna pozostać lista: 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def is_in(first,n):
    p, prev = first, None
    while p != None and p.val < n:
        p, prev = p.next, p
    if p == None or p.val > n and prev != None:
        q = Node(n)
        prev.next = q
        q.next = p
    elif prev == None and p.val != n:
        tmp = p.val
        q = Node(tmp)
        p.next = q.next
        p.val = n
        p.next = q
    return first

def sMnog(f_sort,f_unsort):
    if f_sort == None:
        return "gościu lista ma być niepusta"
    while f_unsort != None:
        f_sort = is_in(f_sort,f_unsort.val)
        f_unsort = f_unsort.next
    return f_sort

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
# x = pushBack(x,5)
# x = pushBack(x,3)
# x = pushBack(x,7)

# write(sMnog(z,x))