# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu.
# Proszę napisać funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

class Node:
    def __init__(self,val=None,prev=None, next=None):
        self.next = next
        self.prev = prev
        self.val = val

# def add(f1,f2):
#     p = f1
#     while f2 != None:
#         s = p.val + f2.val
#         if s > 9: # jeśli coś przechodzi dalej
#             if p.prev != None:
#                 p.prev.val += s//10
#             else: #jeśli nie ma dalej cyfry
#                 p.prev = Node(s//10)
#         p.val = s%10
#         p, f2 = p.prev, f2.prev
#     return f1

def add(l1,l2):
    new = Node("!")
    p = new
    buffer = 0
    while l2 != None and l1 != None:
        s = l1.val + l2.val + buffer
        buffer = s//10
        pointer = Node(s%10)
        p.prev = pointer
        p = p.prev
        l1, l2 = l1.prev, l2.prev
    if l2 != None:
        l2.val += buffer
        p.prev = l2
    elif l1 != None:
        l1.val += buffer
        p.prev = l1
    return new.prev

def pushFront(last,n):
    p,tmp = last, None
    while p != None:
        p, tmp = p.prev, p
    tmp.prev = Node(n)
    return last

def toPrint(last):
    cnt = suma = 0
    while last != None:
        suma += (last.val)*10**cnt
        cnt += 1
        last = last.prev
    return suma

z = Node(1)
z = pushFront(z,2)
# z = pushFront(z,9)
#z = pushFront(z,4)
#z = pushFront(z,5)

x = Node(9)
# x = pushFront(x,9)
#x = pushFront(x,3)
# z = pushFront(z,4)
# z = pushFront(z,5)
    
print(toPrint(x),"+",toPrint(z),"=",toPrint(add(z,x)))




