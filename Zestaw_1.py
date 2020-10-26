def ex3():
#Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
#sumie
    n = int(input("n: "))

    a1 = 1
    a2 = 1
    suma = 1
    b1 = 1
    b2 = 1

    while suma != 0:
    if suma == n:
        print(True)
        break
    suma += a2
    a2, a1 = a1 + a2, a2
    while suma > n:
        suma -= b1
        b2, b1 = b1 + b2, b2
    if suma == 0:
        print(False)

def ex18():
  #Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3
  eps = 0.000001
  n = int(input("n: "))
  x = n
  while abs(n - x**3) > eps:
    x = (1/3)*(2*x + n*x/(x**3))
  print(x)
  
  if __name__ == "__main__":
    ex18()
