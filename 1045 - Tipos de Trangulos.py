C,B,A = sorted(map(float,input().split()))

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == (B ** 2 + C ** 2):
        print("TRIANGULO RETANGULO")
    if A ** 2 > (B ** 2 + C ** 2):
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < (B ** 2 + C ** 2):
        print("TRIANGULO ACUTANGULO")
    if A == B and A == C and B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and C != A) or (B==C and A != B) or (C==A and B != C):
        print("TRIANGULO ISOSCELES")

