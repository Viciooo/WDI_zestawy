# - na liczbych naturalnych określono 3 rodzaje przekształceń:
# a:=a+1
# a:=3*a
# a:=a div 2 (tylko jeżeli liczba a jest parzysta)
# napisać w Pascalu program, który rozstrzyga czy jest mozliwe przekształcenie liczby a w b w serii
# przekształceń o długości nie większej od n, warości a,b,n nalezy wczytać z klawiatury,
# na przykład dla danych a=13 b=11 n=5 odpowiedz brzmi tak bo
# 13->14->7->21->22->11
# dla danych a=13, b=6, n=5 odpowiedź brzmi nie

def A(x):
    return x+1

def B(x):
    return x*3

def C(x):
    return x//2 if x % 2 == 0 else x

def Do(a,b,n):
    if a == b:
        return True
    if n == 0:
        return False
    return Do(A(a),b,n-1) or Do(B(a),b,n-1) or Do(C(a),b,n-1)

print(Do(13,6,5))
    


