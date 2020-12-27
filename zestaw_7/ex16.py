# Zadanie 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej,
# przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.

class Node():
    def __init__(self,val=None):
        self.next = None
        self.val = val

def Count5_inSys8(n):
    cnt = 0
    while n != 0:
        if n % 8 == 5:
            cnt += 1
        n //= 8
    return cnt % 2 == 0

def add_front(first,n):
    q = Node(n)
    q.next = first 
    return q

def func(first):
    p, prev = first, None
    if Count5_inSys8(p.val):
        p, prev = p.next, p
    write(first)
    while p!= None:
        if Count5_inSys8(p.val):
            first = add_front(first,p.val)
            prev.next, p = p.next, p.next
        else:
            p, prev = p.next, p
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

# write(z1)
# print("**********")
write(z2)
print("**********")
write(func(z2))

