# Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.

class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def add_front(first,n):
    q = Node(n)
    q.next = first 
    return q

def reverse(first):
    p = first
    z = None
    while p!= None:
        z = add_front(z,p.val)
        p = p.next
    return z

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

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

write(z1)
print("**********")
write(z2)
print("**********")
write(reverse(z2))