# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def iter_merge(f1,f2):
    z = Node("!") # wartownik ale chill usunie się
    p = z
    while f1 != None and f2 != None:
        if f1.val < f2.val:
            p.next = Node(f1.val)
            p = p.next
            f1 = f1.next
        elif f1.val == f2.val:
            p.next = Node(f2.val)
            f1, f2, p = f1.next, f2.next, p.next
        else:
            p.next = Node(f2.val)
            p, f2 = p.next, f2.next

    while f1 != None:
        p.next = Node(f1.val)
        p = p.next
        f1 = f1.next

    while f2 != None:
        p.next = Node(f2.val)
        p = p.next
        f2 = f2.next

    if f1 == f2 == None:
        return z.next

null = None
def reku(first,second,new_last):
    if first==null:
        if second!=null:
            buffer = second.next
            second.next = null
            new_last.next = second
            return reku(first,buffer,second)
        else:
            return
    if second==null:
        if first!=null:
            buffer = first.next
            first.next = null
            new_last.next = first
            return reku(buffer,second,first)
        else:
            return 
    if first.val>second.val:
        buffer = second.next
        second.next = null
        new_last.next = second
        return reku(first,buffer,second)
    else:
        new_last.next = first
        buffer = first.next
        first.next = null
        return reku(buffer,second,first)
def rec_merge(first,second):
    new_ = Node()
    reku(first,second,new_)
    return new_.next
#podpierdoloned od ŁP

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

def insert(space,n):
    p = space #space - nasz zbiór
    prev = None

    while p != None and p.val < n:
        prev = p
        p = p.next
    
    if p != None and p.val == n: #przypadek gdy taka wartość w zbiorze już istnieje
        return space

    q = Node(n)
    if prev == None: # wstawianie na początku - nie ma po co sprawdzać czy 
        q.next = p   #lista pusta bo if zadziała tak samo w obu przypadkach
        return q
    
    prev.next = q
    q.next = p
    return space


z1 = insert(None,11)
z1 = insert(z1,3)
z2 = insert(None,7)
z2 = insert(z2,1)
z2 = insert(z2,2)
z2 = insert(z2,5)

write(z1)
print("**********")
write(z2)
print("**********")
z3 = iter_merge(z1,z2)
write(z3)

