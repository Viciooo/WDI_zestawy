# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu.
# Proszę napisać funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

def sumOfLists(f1,f2):
    p = f1
    while p != None and f2 != None:
        p.val += f2.val
        p, f2 = p.next, f2.next
    return f1
