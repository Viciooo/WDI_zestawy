# Zadanie 15. Proszę napisać funkcję, która otrzymując jako parametr wskaźnik na początek listy jednokierunkowej,
# usuwa z niej wszystkie elementy,w których wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

class Node():
    def __init__(self,val=None):
        self.next = None
        self.val = val

def Count(n):
    cnt1 = cnt2 = 0 
    while n != 0:
        if n % 3 == 1:
            cnt1 += 1
        elif n % 3 == 2:
            cnt2 += 1
        n //= 3
    return cnt1 > cnt2

def func(first):
    p, prev = first, None
    if Count(p.val):
        p, first = p.next, first.next
    while p != None:
        if Count(p.val):
            prev.next, p = p.next, p.next
        else:
            p, prev = p.next, p
    return first

# #################### test1
# [1] -----> [2] -----> [5] -----> [7] -----> None
# **********
# [2] -----> [5] -----> [7] -----> None
# #################### test2
# [1] -----> [2] -----> [4] -----> [7] -----> None
# **********
# [2] -----> [7] -----> None