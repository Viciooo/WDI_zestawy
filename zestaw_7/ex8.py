# Zadanie 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. 
# Do funkcji należy przekazać wskazanie na pierwszy element listy.
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

def pop_odd(first):
    p, prev, cnt = first, None, 0
    while p != None:
        if cnt%2 == 1:
            prev.next = p.next
        p, prev, cnt = p.next, p, cnt+1
    return first

# def write(first):
#     while first != None:
#         print("[",first.val,"] -----> ",end='',sep='')
#         first = first.next
#     print(None)

# def insert(space,n):
#     p = space #space - nasz zbiór
#     prev = None

#     while p != None and p.val < n:
#         prev = p
#         p = p.next
    
#     if p != None and p.val == n: #przypadek gdy taka wartość w zbiorze już istnieje
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

# # write(z1)
# # print("**********")
# write(z2)
# print("**********")
# z2 = pop_odd(z2)
# write(z2)