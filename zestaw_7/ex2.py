# Zadanie 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. 
# Proszę napisać trzy funkcje: 
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n, 
# – podstawiającą wartość value pod indeks n.

class Cell ():
    def __init__(self,val=0,indeks=0):
        self.val = val
        self.indeks = indeks
        self.next = None

def init():
    return Cell("!")

def search (first,n):
    while first != None and first.indeks < n :
        first = first.next
    if first == None : return "Not found"
    return first.val

def insert(first,ind,val):
    prev = None
    p = first
    while p != None and p.indeks < ind :
        prev,p = p,p.next
    if p != None and p.indeks == ind:   # znaleźliśmy indeks i podmieniamy
        p.val = val
        return first
    q = Cell(val,ind)
    if prev == None:   # dodajemy na początku (bo pusty lub najmniejszy indeks)
        q.next = p
        return q
    prev.next = q         # dodajemy w środku i na końcu
    q.next = p
    return first


def write(first):
    if first.val == "!" :
        first = first.next
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

first = init()
first = insert(first,5,15)
first = insert(first,7,16)
first = insert(first,5,30)
first = insert(first,1,12)
first = insert(first,3,9)
write(first)



    



