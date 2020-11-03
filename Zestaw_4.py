def ex1():
#Zadanie 1. Dana jest tablica T[N][N]. Prosze napisac funkcje wypełniajaca tablice kolejnymi liczbami
#naturalnymi po spirali.
    N = 5 # dim tablicy
    k = 2 #wartość od której startujemy
    t = N*[0]

    for i in range(N):  #t[row][column]
        t[i] = N*[0]
    t[0][0] = 1
    
    #rowsAmt = N - 1 # ilośc znaków do wpisania w rzędzie
    #columnsAmt = N - 2 # ilośc znaków do wpisania w kolumnie - startowo
    r = 0 #row index
    c = 0 #column index

    while k  <= N*N:

        while c+1< N and t[r][c+1] == 0: # w prawo
            c += 1
            t[r][c] = k
            k += 1

        while r+1 < N and t[r+1][c] == 0: # w dół
            r += 1
            t[r][c] = k
            k += 1

        while c-1 >= 0 and t[r][c-1] == 0: # w lewo
            c -= 1
            t[r][c] = k
            k += 1

        while r-1 >= 0 and t[r-1][c] == 0: #do góry
            r -= 1
            t[r][c] = k
            k += 1

    
    
    for i in range(len(t)):
       print(t[i])

if __name__ == "__main__":
    ex1()
