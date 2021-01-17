# Zadanie 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych.
# Proszę napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]

class Node():
    def __init__(self,l=None,r=None,next=None):
        self.l = l
        self.r = r
        self.next = next

def func(pointer): 
# ta funkcja sprawdza czy next przedziały mogą poszerzyć obecnie przerabiany przedział
#jeśli tak to usuwa je i poszerza przedział [l,r] i zwiększa licznik akcji (cnt) o jeden
    global cnt
    p, prev = pointer.next, pointer
    l, r = pointer.l , pointer.r
    if p == None: # gdy jest tylko jeden przedział po przerabianym
        if prev.r > r and prev.l <= r:
            cnt += 1
            if prev.l <= l:
                l, r = prev.l, prev.r
            else:
                r = prev.r
            return None
        elif prev.l < l and prev.r >= l:
            cnt += 1
            l = prev.l
            return None
    while p != None:
        if p.r >= r and p.l <= r:
            cnt += 1
            if p.l <= l:
                l, r = p.l, p.r
            else:
                r = p.r
            prev.next = p.next
        elif p.l <= l and p.r >= l:
            cnt += 1
            l = p.l
            prev.next = p.next
        p, prev = p.next, p
    pointer.l, pointer.r = l, r
    return pointer

def check(pointer):
#'stripuje' z przedziałów zawierających się w innych
    prev, p = pointer, pointer.next
    l, r = pointer.l, pointer.r
    while p != None:
        if p.l >= l and p.r <= r:
            prev.next = p.next
        p, prev = p.next, p
    return pointer

def loop(first):
#wywołuje check dla każdego przedziału
    p = first
    while p != None:
        p = check(p)
        p = p.next
    return first

def simplify(first):
#funckja główna - wykonuje się tak długo, aż może uprościć l. przedziałów
#jeśli cnt == 0 po wykonaniu obrotu pętli to oznacza, że żadna zmiana nie
#została wykonana w tym obrocie - czyli nie da się uprościć bardziej l. przedziałów
    global cnt
    while True:
        p = first
        cnt = 0
        while p!= None:
            p = func(p)
            p = p.next
        if cnt == 0:
            break
    return loop(first)

def pushBack(first,l,r):
#funkcja do wpychania el na koniec listy - potrzebna tylko do testów
    p = first
    prev = None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(l,r)
    return first

    
# [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]

z = Node(15,19)
z = pushBack(z,2,5)
z = pushBack(z,7,11)
z = pushBack(z,6,7)
z = pushBack(z,8,12)
z = pushBack(z,5,6)
z = pushBack(z,13,17)
z = pushBack(z,12,13)
z = pushBack(z,12,12)

def write(first):
    while first != None:
        print("[",first.l,",",first.r,"] -----> ",end='',sep='')
        first = first.next
    print(None)

write(z)
write(simplify(z))

