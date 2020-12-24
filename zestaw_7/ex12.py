# Zadanie 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
# Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz 
# funkcję dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis,
# funkcja powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.

class Node():
    def __init__(self,val=None):
        self.next = None
        self.val = val

def strCompare(sInput,sOfList):
    for i in range(len(min(sInput,sOfList))):
        if ord(sInput[i:i+1]) < ord(sOfList[i:i+1]):
            return True
        if ord(sInput[i:i+1]) > ord(sOfList[i:i+1]):
            return False

def insert(first,sInput):
    p, prev = first, Node("!")
    prev.next = p
    f, q = prev, Node(sInput)
    if p != None and strCompare(sInput,p.val): #wstawiamy przed
        prev.next, q.next = q, p
        return f.next
    while p!= None:
        if strCompare(sInput,p.val):
            prev.next, q.next = q, p
            return f.next
        p, prev = p.next, p

    prev.next = q
    return f.next

z = insert(None,"abc")
z = insert(z,"aaa")
z = insert(z,"aed")
z = insert(z,"acd")
z = insert(z,"aaaa")
def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)

write(z)

