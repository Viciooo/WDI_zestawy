# Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.

#nie działa z ćw garka :(
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def reverse(ptr):
    firsts = [None for _ in range(10)]
    lasts = [None for _ in range(10)]

    while ptr != None:
        last_dig = ptr.val % 10
        if firsts[last_dig] == None:
            firsts[last_dig] = lasts[last_dig] = ptr
        else:
            lasts[last_dig].next = ptr
            lasts[last_dig] = ptr
        ptr = ptr.next
    
    first = None
    for i in range(10):
        if firsts[i] != None:
            if first == None:
                first = firsts[i]
                last = lasts[i]
            else:
                last.next = firsts[i]
                last = lasts[i]
    last.next = None
    return first

    # first = None
    # for i in range(9,-1,-1):
    #     if firsts[i] != None:
    #         lasts[i].next = first
    #         first = firsts[i]
    # return first


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

