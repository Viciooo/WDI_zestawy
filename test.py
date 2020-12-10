
#Zadanie 24. Tablica T = [(x1, y1), (x1, y1), ...] zawiera połozenia N punktów o współrzednych opisanych
#wartosciami typu float. Prosze napisac funkcje, która zwróci najmniejsza odległosc miedzy srodkami ciezkosci
#2 niepustych podzbiorów tego zbioru.
def massMiddle(t):
    x, y = 0, 0
    for i in t:
        x += i[0]
        y += i[1]
    x /= len(t)
    y /= len(t)
    return x,y

def odl(t1,t2):
    m1 = massMiddle(t1)
    m2 = massMiddle(t2)
    r = ((m1[0]-m2[0])**2 + (m1[1]-m2[1])**2)**(1/2)
    return r

def ex24(T,t1=[],t2=[],i=0):
    global x
    if len(t1) > 0 and len(t2) > 0:
        tmp = odl(t1,t2)
        if tmp < x:
            x = tmp
    if i == len(T):
        return False
    return ex24(T,t1+[T[i]],t2,i+1) | ex24(T,t1,t2+[T[i]],i+1) | ex24(T,t1,t2,i+1)

def start24(T):
    global x
    x = 1000
    ex24(T)
    return x

t = [(1,4),(1,2)]
print(start24(t))