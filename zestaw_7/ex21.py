# Zadanie 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą.
# Warunkiem usunięcia jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.
class Node():
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val


def search(first):
    p, prev, l  = first.next, first, None
    m_cnt = 1
    cnt = 1
    flag = True
    while p != None:
        if cnt == 1:
            pr_ciagu = l
            p_ciagu = prev
        if p.val > prev.val:
            cnt += 1
        else:
            if cnt == m_cnt:
                flag = False
            elif cnt > m_cnt:
                m_cnt = cnt
                m1 = p_ciagu
                m2 = pr_ciagu
                flag = True
            cnt = 1
        p, prev, l = p.next, p, prev
    if flag and cnt != m_cnt:
        while m1 != None and m_cnt > 0:
            m_cnt -= 1
            m2.next = m1.next
            m1 = m1.next
    return first
    

def pushBack(first,n):
    p, previous = first, None
    while p != None:
        p, previous = p.next, p
    previous.next = Node(n)
    return first

def write(first):
    while first != None:
        print("[",first.val,"] -----> ",end='',sep='')
        first = first.next
    print(None)


z = Node(3)
z = pushBack(z,1)
z = pushBack(z,2)
z = pushBack(z,3)
z = pushBack(z,4)
z = pushBack(z,3)
z = pushBack(z,8)
#z = pushBack(z,1)
write(z)

write(search(z))