'''Zadanie 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru'''

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

def search(element,p):
# element - obiekt szukany w liście odsyłaczowej
#i - wskaźnik do listy odsyłaczowej
    while p != None:
        if p.value == element:
            return True
        p = p.next
    return False

def insert(space,n):
#traktujemy to jako zbiór - więc trzeba sprawdzić czy element już nie istnieje w zbiorze
#zbiór implementujemy jako posortowaną listę odsyłaczową
    
    p = space #space - nasz zbiór
    prev = None

    while p != None and p.value < n:
        prev = p
        p = p.next
    
    if p != None and p.value == n: #przypadek gdy taka wartość w zbiorze już istnieje
        return space

    # niżej przypadki gdy dodajemy element

    q = Node(n)
    if prev == None: # wstawianie na początku - nie ma po co sprawdzać czy 
        q.next = p   #lista pusta bo if zadziała tak samo w obu przypadkach
        return q

    # jeśli nie wstawiamy na początku to wstawiamy w środku bądź na końcu
    #te przypadki różnią się tym, że przy wstawianiu na końcu nie musimy
    #ustawiać wskaźnik q.next = p - czyli wskazania na następny element
    #bo następny element to None
    #Jeżeli wstawiamy na końcu, to potrzebujemy tego wskaźnika aby mieć zbiór połączony
    
    prev.next = q
    q.next = p
    return space

def delete(space, n): #dlaczego nie działa usunięcie z pierwszego miejsca ? i co robić jak chcemy usunąć jedyny element w liście?
    if space is None:
        return space
    prev = None
    curr = space
    if curr.value == n:
        curr = curr.next
        return curr
    while curr is not None and curr.value != n:
        prev = curr
        curr = curr.next
    if curr is None:
        return space
    prev.next = curr.next
    return space

def print_all(p):
    while p != None:
        print("[",p.value,"]",sep='',end=" -> ")
        p = p.next
    print(None)

z1 = insert(None,2)
#z1 = insert(z1,3)
# z1 = insert(z1,7)
# z1 = insert(z1,1)
# z1 = insert(z1,2)
# z1 = insert(z1,5)
z1 = delete(z1,2)

print_all(z1)