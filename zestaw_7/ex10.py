# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu.
# Proszę napisać funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def Add(f1,f2):
    new = Node("!")
    p = new
    buffor = 0

    while f1 != None and f2 != None:
        suma = f1.val + f2.val + buffor
        buffor = suma // 10
        q = Node(suma%10)
        p.next = q
        p, f1, f2 = p.next, f1.next, f2.next

    while f1 != None:
        suma = f1.val + buffor
        buffor = suma // 10
        q = Node(suma%10)
        p.next = q
        p, f1= p.next, f1.next
        
    while f2 != None:
        suma = f2.val + buffor
        buffor = suma // 10
        q = Node(suma%10)
        p.next = q
        p, f2= p.next, f2.next
    
    if buffor > 0:
        q = Node(buffor)
        p.next = q

    return new.next

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

f1 = Node(8)
f1.next = Node(9)
f1.next.next = Node(9)
f2 = Node(2)
wynik = Add(f1,f2)
write(wynik)

