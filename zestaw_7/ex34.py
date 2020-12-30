# Zadanie 34. 
# Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje dokładnie k razy.
# Do funkcji należy przekazać wskazanie na jeden z elementów listy,
# oraz liczbę k, funkcja powinna zwrócić informację czy usunięto jakieś elementy z listy.

class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def count(first,v): #liczy występowanie cyfry w liście cyklicznej
    p, prev, cnt = first.next, first, 0
    while p != first:
        if prev.val == v:
            cnt += 1
        p, prev = p.next, p
    if prev.val == v:
        cnt += 1
    return cnt

def deleteVal(first,v,k): 
#k ma przyspieszyć działanie - funkcja ma się skończyć gdy k == 0 bo nie ma już wartości v
#nie wiem tylko czy sprawdzanie tego warunku za każdym razem nie jest cięższe niż przelecenie do końca listy 
#pewnie czasami tak a czasami nie
    p, prev = first.next, first
    while p != first and k != 0:
        if p.val == v:
            k -= 1
            prev.next, p = p.next, p.next
        else:
            p, prev = p.next, p
    if p.val == v:
        k-= 1
        prev.next, p = p.next,p.next
    if p.next == p:
        return p
    return p


def deleteSelected(first,k):
    deleted = end = False
    v = -1
    while end != True and first != None:
        p, prev, end = first.next, first, True
        while p != first: #pewnie da się szybciej tj zmienić wskaźnik p na nowy po usunięciu
            if count(first,prev.val) == k:
                v = prev.val
                deleted, end = True, False
                first = deleteVal(p,prev.val,k)
                break
            p, prev = p.next, p
    print(deleted)
    if v == first.val and end == True:
        return None
    return first

def insert(p,s):
    if p == None: #lista pusta
        return Node(s)
    curr, prev, q = p.next, p, Node(s)
    if curr == None: #lista ma jeden element
        prev.next, q.next = q, prev
        return q  
    #jeśli dodaje "na koniec cyklu"
    prev.next, q.next = q, curr
    return q

# def writeCycle(first):
#     if first == None:
#         print(None)
#         return
#     p, prev = first.next, first
#     while p != first:
#         print("[",prev.val,"] -----> ",end='',sep='')
#         p, prev = p.next, p

#     print("[",prev.val,"] -----> ",sep='')

# z = None
# z = insert(z,1)
# z = insert(z,2)
# z = insert(z,2)
# z = insert(z,1)
# z = insert(z,7)
# z = insert(z,2)
# z = insert(z,1)
# # z = insert(z,5)
# # z = insert(z,1)

# writeCycle(z)
# writeCycle(deleteSelected(z,3))
