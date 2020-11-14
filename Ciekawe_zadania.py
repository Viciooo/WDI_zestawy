def ex1():
#Prosze napisac w jezyku Python program, który wyznacza ostatnia niezerowa cyfra N! Program powinien
#działac dla N rzedu 3000.
    N = 30000
    x = 0
    y = 1
    while N != 1:
        if N % 5 ==0:
            N //= 5
            x += N
        else:
            y *= N%10
            N -= 1
    if x % 4 == 0:
        x = 0
    print(((2**x)*y)%10)
