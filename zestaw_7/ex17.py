# Zadanie 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej,
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

class Node():
    def __init__(self,val=None,next=None,prev=None):
        self.next = next
        self.prev = prev
        self.val = val
    
def Count1(n):
    cnt = 0
    while n!= 0:
        if n % 2 == 1:
            cnt +=1 
        n //= 2
    return cnt%2 == 1

def func(first):
    p = first
    while p != None:
        if Count1(p.val):
            if p.prev == None:
                p.next.prev, first = None, p.next
            elif p.next == None:
                p.prev.next = None
            else:
                p.prev.next, p.next.prev = p.next, p.prev
        p = p.next
    return first

def popByVal(f,n):
    #f - first, n - val
    p = f
    while p != None:
        if p.val == n:
            if p.prev == None:
                f = f.next
            elif p.next == None:
                p.prev.next = None
            else:
                p.prev.next = p.next
                p.next.prev = p.prev
        p = p.next
    return f


z = Node(11)
for i in range(10):
    a = Node(i, z, None)
    z.prev = a
    z = a

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

z = popByVal(z,5)
write(func(z))