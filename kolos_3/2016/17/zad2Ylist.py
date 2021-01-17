class Node:
    def __init__(self,val,next=None):
        self.next = next
        self.val=val

def getLen(p):
    cnt = 0
    while p != None:
        cnt += 1
        p = p.next
    return cnt

def splitANDcnt(f1,f2):
    if f1 == f2:
        new = Node("!")
        prev1, p1 = new, f1
        while p1 != None:
            q = Node(p1.val)
            prev1.next = q
            prev1, p1 = prev1.next, p1.next
        return new.next, f2, getLen(f1)

    l1, l2, cnt = getLen(f1), getLen(f2), 0
    p1, prev1, p2 = f1, None, f2

    while l1 > l2:
        p1, prev1 = p1.next, p1
        l1 -= 1
    while l2 > l1:
        p2 = p2.next
        l2 -= 1
    
    while p1 != p2:
        p1, prev1, p2 = p1.next, p1, p2.next

    while p1 != None:
        cnt += 1
        q = Node(p1.val)
        prev1.next = q
        prev1, p1 = prev1.next, p1.next
    return f1, f2, cnt


# wspolna = Node(1,Node(2,Node(3,Node(4,Node(5,Node(7,None))))))
# first = Node(6,Node(9,Node(10,Node(11,wspolna))))
# second = Node(0,Node(8,Node(10,wspolna)))
f1 = Node(6,Node(9,Node(10,Node(11))))
f2 = Node(0,Node(8,Node(10)))

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

f1, f2, cnt = splitANDcnt(f1,f2)

# f1.next.next.next.next.next.next.val = 55
# write(f1)
# print("***********")

# write(f2)
# print("***********")

# print(cnt)

# first,second,cnt=func2(wspolna,wspolna)
print(cnt)
f1.next.next.val = 95
write(f1)
write(f2)