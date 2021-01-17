# Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.

#nie działa z ćw garka :(
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def reverse (first) :
    if first == None or first.next == None :
        return first
    p = first.next
    prev = first
    first.next = None
    while p != None :
        prev,p = p,p.next
        prev.next = first
        first = prev
    return first


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

def write(first):
    if first.val == "!" :
        first = first.next
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

# z1 = insert(None,11)
# z1 = insert(z1,3)
z2 = insert(None,7)
z2 = insert(z2,1)
z2 = insert(z2,2)
z2 = insert(z2,5)

# write(z1)
# print("**********")
write(z2)
print("**********")
# z3 = merge_rek(z1,z2)
write(reverse(z2))

