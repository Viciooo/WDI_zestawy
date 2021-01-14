class klocek:
    def __init__(self,a=None, b=None, next=None):
        self.a = a
        self.b = b
        self.next = next

def pushBack(first,A,B):
    p, prev, q = first, None, klocek(A,B)
    while p != None:
        p, prev = p.next, p
    if prev == None:
        p.next == q
    else:
        prev.next = q
    return first

def write(first):
    while first != None:
        print("[",first.a,"|",first.b,"] -----> ",end='',sep='')
        first = first.next
    print(None)

m = klocek(2,9)
m = pushBack(m,3,6)
m = pushBack(m,8,2)
m = pushBack(m,2,3)
m = pushBack(m,6,2)

write(m)