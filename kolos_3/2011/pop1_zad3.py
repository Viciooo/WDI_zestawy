# 3. Mamy 2 uporządkowane listy jednokierunkowe. Napisz funkcję, która zwróci wskaźnik na różnicę
# symetryczną z obu list (czyli taki XOR).

#malejaco

class Node:
    def __init__(self,val,next=None):
        self.next = next
        self.val=val

def diff(f1,f2):
    new = Node("!")
    q = new
    while f1 != None and f2 != None:
        if f1.val > f2.val:
            q.next = f1
            f1 = f1.next
        elif f2.val > f1.val:
            q.next = f2
            f2 = f2.next
        else:
            q.next = f1
            f1, f2 = f1.next, f2.next
        q = q.next
    if f1 != None:
        q.next = f1
        q = q.next
    elif f2 != None:
        q.next = f2
        q = q.next
    q = q.next
    return new.next

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

l1 = Node(10)
l1 = pushBack(l1,4)
l1 = pushBack(l1,3)
l1 = pushBack(l1,2)
# l1 = pushBack(l1,8)
# l1 = pushBack(l1,15)
# l1 = pushBack(l1,23)
l2 = Node(15)
l2 = pushBack(l2,5)
# l2 = pushBack(l2,1)
# l2 = pushBack(l2,0)
# l2 = pushBack(l2,13)
# l2 = pushBack(l2,20)
# l2 = pushBack(l2,23)

write(diff(l1,l2))