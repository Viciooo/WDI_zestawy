# Zadanie 11. Lista zawiera niepowtarzające się elementy.
# Proszę napisać funkcję do której przekazujemy wskaźnik na początek oraz wartość klucza.
# Jeżeli element o takim kluczu występuje w liście należy go usunąć z listy.
# Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.

class Node():
    def __init__(self,key=None):
        self.next = None
        self.key = key

def weirdTask(first,k):
    p, prev = first, None

    if p.key == k:
        return first.next

    while p != None and p.key < k:
        p, prev = p.next, p

    if p != None and p.key == k :
        prev.next = p.next
        return first

    else:
        q = Node(k)
        prev.next = q
        q.next = p
        return first

# def insert(space,n):
#     p = space #space - nasz zbiór
#     prev = None

#     while p != None and p.key < n:
#         prev = p
#         p = p.next
    
#     if p != None and p.key == n: #przypadek gdy taka wartość w zbiorze już istnieje
#         return space

#     q = Node(n)
#     if prev == None: # wstawianie na początku - nie ma po co sprawdzać czy 
#         q.next = p   #lista pusta bo if zadziała tak samo w obu przypadkach
#         return q
    
#     prev.next = q
#     q.next = p
#     return space


# z1 = insert(None,11)
# z1 = insert(z1,3)
# z2 = insert(None,7)
# z2 = insert(z2,1)
# z2 = insert(z2,2)
# z2 = insert(z2,5)

# def write(first):
#     while first != None:
#         print("[",first.key,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

# # write(z1)
# # print("**********")
# write(z2)
# print("**********")
# write(weirdTask(z2,1))
