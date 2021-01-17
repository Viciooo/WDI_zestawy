# 2. Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej
# rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
# Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
# występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self,val,next=None):
        self.next = next
        self.val=val
    def __str__(self):
        return f"{self.val}-->"

class lista:
    def __init__(self, first=None):
        self.first = first

    def __str__(self):
        cp = self.first
        if cp == None:
            return "List is empty!"
        cp2 = self.first.next
        ret = str(cp)
        while cp != cp2:
            ret = ret + str(cp2)
            cp2 = cp2.next
        return ret

def moveToFront(f):
    prev, p = f, f.next
    while prev.val < p.val:
        p, prev = p.next, p
    return prev, p

def delete(f1,f2):
    prev1, p1 = moveToFront(f1)
    prev2, p2 = moveToFront(f2)
    f1, f2 = prev1, prev2
    cnt = 0
    flag = False
    while p1 != f1 and p2 != f2:
        if p1.val == p2.val:
            prev1.next, p1, prev2.next, p2 = p1.next, p1.next, p2.next, p2.next
            cnt += 2
        elif p1.val < p2.val:
            p1, prev1 = p1.next, p1
        else:
            p2, prev2 = p2.next, p2
    if p1.val == p2.val:
        flag = True
        cnt += 2
        prev1.next, p1, prev2.next, p2 = p1.next, p1.next, p2.next, p2.next
    if flag == True and p1 == p1.next:
        p1 = None
    if flag == True and p2 == p2.next:
        p2 = None
    return cnt, p1, p2

def tabToCycleLink(tab):
    first = Node(tab[0], None)
    a = first
    for i in range(1, len(tab)):
        a.next = Node(tab[i], None)
        a = a.next
    a.next = first
    return first


tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,0]
tab2 = [11, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret, f1, f2 = delete(tabToCycleLink(tab1), tabToCycleLink(tab2))
print(ret)
print(lista(f1),"\n", lista(f2), sep="")