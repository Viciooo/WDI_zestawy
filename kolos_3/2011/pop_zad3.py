# 3. Dane są dwa niepuste łańcuchy odsyłaczowe [jednokierunkowe] przechowujące liczby
# naturalne. W pierwszym liczby są uporządkowane rosnąco, a w drugim malejąco. Proszę
# napisać odpowiednie definicje typów oraz funkcję scalającą takie dwa łańcuchy w jeden
# zawierający posortowane rosnąco elementy. Funkcja powinna zwrócić wskaźnik do nowego
# łańcucha.

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def ex1(l1,l2):
    #l1 jest rosnąca
    #l2 malejąca
    last, prev = l2.next, l2

    while last != None:
        last, prev = last.next, last
    last = prev

    p1 = l1 
    n = Node("!")
    new = n
    flag = True
    end = None

    while p1 != None and end != l2:

        if flag == False: #jeśli była przesuwana lista2
            last, prev2 = l2, None
            while last != end:
                last, prev2 = last.next, last
            last = prev2

        if p1.val == last.val: #są równe obie przesuwamy
            end = last
            flag = False
            new.next, p1 = p1, p1.next

        elif p1.val < last.val: #p1 przesuwamy
            new.next, p1 = p1, p1.next

        else:
            end = last
            flag = False
            new.next = last
        new = new.next

    if p1 != None: #dodajemy p1
        new.next = p1
        new.next.next = None

    elif last != l2: #dodajemy l2 na koniec
        while last != l2:
            last, prev2 = l2, None
            while last != end:
                last, prev2 = last.next, last
            last = prev2
            end = last
            new.next = last
            new = new.next
        new.next = None

    else:
        new.next = None
    return n.next


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

l1 = Node(1)
l1 = pushBack(l1,2)
l1 = pushBack(l1,3)
l1 = pushBack(l1,7)

l2 = Node(15)
l2 = pushBack(l2,12)
# l1 = [1,2,3,7]
# l2 = [15,12]
# l2 = pushBack(l2,11)
# l2 = pushBack(l2,8)
# l2 = pushBack(l2,1)
# l2 = pushBack(l2,0)

write(l1)
print("***********")
write(l2)
print("***********")
write(ex1(l1,l2))