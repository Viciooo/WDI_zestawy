# 3. Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2).
# struct klocek {
#  int a;
#  int b;
#  klocek *next;
# };
# Lista zawiera zestaw klocków, które można ułożyć w ciąg. Niestety klocki pomieszały się. Proszę napisać funkcję,
# która ustawia klocki na liście w ciąg. Uwaga: orientacja klocków w liście jest właściwa.
# Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
# należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]

class Node:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
        self.next = None


def solve(l):
    p = l
    leng = 0
    while p != None:
        leng += 1
        p = p.next
    del p
    def rek(l, curr, ignore, leng):
        if leng == 0:
            curr.next = None
            return True
        start = l
        while l != None:
            if l.a == curr.b and l not in ignore or curr.b == None:
                if rek(start, l, [*ignore, l], leng-1):
                    curr.next = l
                    return True
            l = l.next
        return False
    q = Node()
    q.next = l

    rek(l, q, [], leng)
    return q.next

def pushBack(first,a,b):
    p = first
    prev = None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(a,b)
    return first

def write(first):
    while first != None:
        print("[",first.a,",",first.b,"] -----> ",end='',sep='')
        first = first.next
    print(None)

lista = Node(2,9)
lista = pushBack(lista,3,6)
lista = pushBack(lista,8,2)
lista = pushBack(lista,2,3)
lista = pushBack(lista,6,2)

write(solve(lista))

#zrobione przez Bartłomieja Wiśniewskiego