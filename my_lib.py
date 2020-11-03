#Moduł przydatnych funkcji

def Split(word): 
    return [char for char in word]

def StringCompare(string1,string2):
    
    cnt = 0
    l1 = split(string1)
    l2 = split(string2)

    print(l1,l2)

    if len(l1) > len(l2):
        length = len(l1)
    else:
        length = len(l2)

    for i in range(length):
        if l1[i] != l2[i]:
            break
        print(">>", cnt)
        cnt += 1

    print("Są podobne do :", cnt, "miejsca")

def InsertionSort(arr): 
    for i in range(1, len(arr)):  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

def GenRndTab(length,start,end):
    from random import randint
    tab = []
    for i in range(length):
        tab.append(randint(start,end))
    return tab

def IfPrime(n):
    k = 2

    if(n==1):
        return False

    while k <= n**0.5:

        if n % k == 0:

            if n // k == 1:
                return True
            else:
                return False
        k += 1

    return True

def ToBinary(n,length):
    l =[]
    while n // 2 != 0:
        l.append(n%2)
        n //=2
    l.append(n%2)
    while len(l)<length:
        l.append(0)
    return l

def DivList(n):
    l = []
    for i in range(2,n+1):
        if n % i == 0:
            l.append(i)
        while n % i == 0:
            n //= i
    return l
