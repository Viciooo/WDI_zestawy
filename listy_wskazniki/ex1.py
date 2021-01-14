# 2. Zbiór liczb naturalnych jest reprezentowany jako jednokierunkowa lista.
# Y-lista to struktura reprezentująca dwa zbiory liczb naturalnych (rysunek).
# Proszę napisać funkcję, która dwa zbiory A,B reprezentowane jako Y-lista przekształca
# w dwa zbiory reprezentowane jako niezależne listy. Do funkcji należy przekazać wskaźniki do dwóch list,
# funkcja powinna zwrócić liczbę elementów części wspólnej zbiorów A,B. Uwagi: - ważne:
# jeżeli część wspólna dwóch zbiorów jest pusta, Y-lista staje się dwoma niezależnymi listami. - wartości w listach nie są uporządkowane

#chyba chodzi o to żeby pozbyć się przekazywania wartości części listy przez referencję - w pythonie nie ma to sensu bo przekazuje się to przez wartość, ale no i tak zrobione
class Node:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val

def is_in(pointer,v):
    #szuka wartości w liście pointer, jeśli jest to usuwa jeśli nie to zwraca false
    p, prev = pointer, None
    while p != None:
        if p.val == v:
            if prev == None:
                return pointer.next
            else:
                prev.next, p = p.next, p.next
                return pointer
        p, prev = p.next, p
    return False

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def pushFront(first,n):
    q = Node(first.val)
    q.next = first.next
    first.val = n
    first.next = q
    return first
    

def ex1(first1,first2):
    p, prev = first1, None
    cnt = 0
    common = Node("!")
    while p != None:
        wynik = is_in(first2,p.val)
        if wynik != False:
            write(p)
            first2 = wynik
            common = pushFront(common,p.val)
            cnt += 1
            if prev == None:
                first1, p = first1.next, p.next
            else:
                prev.next, p = p.next, p.next
            write(p)
        else:
            p, prev = p.next, p

    tmp = common
    while tmp.val != "!":
        first1 = pushFront(first1,tmp.val)
        first2 = pushFront(first2,tmp.val)
        tmp = tmp.next
    
    write(first1)
    write(first2)

    return cnt

x = Node(5)
x = pushBack(x,11)
x = pushBack(x,3)
x = pushBack(x,2)

y = Node(13)
y = pushBack(y,13)
y = pushBack(y,7)
y = pushBack(y,17)
y = pushBack(y,3)
y = pushBack(y,2)

write(x)
write(y)
print("***********")
print(ex1(x,y))