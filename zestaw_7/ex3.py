# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.
end = None
class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
def scal(f1,f2):
    f = Node()
    l = f
    while f1 != None and f2 != None:
        if f1.val < f2.val:
            l.next = f1
            l = f1
            f1 = f1.next
        else:
            l.next = f2
            l = f2
            f2 = f2.next
        end
    end
    if f1 != None:
        l.next = f1
    else:
        l.next = f2
    end
    return f.next
end

def merge_rek(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    if l1.val < l2.val:
        res = l1
        res.next = merge_rek(l1.next, l2)
    else:
        res = l2
        res.next = merge_rek(l1, l2.next)
    
    return res

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
z3 = merge_rek(z1,z2)
write(z3)

