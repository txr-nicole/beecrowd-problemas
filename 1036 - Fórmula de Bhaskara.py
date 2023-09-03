numeros = input().split()

A = float(numeros[0])
B = float(numeros[1])
C = float(numeros[2])
delta = B**2 - 4*A*C
if (delta == 0 or delta < 0 or A == 0):
    print('Impossivel calcular')
else:
    R1 = (-B + delta**0.5)/ (2*A) 
    R2 = (-B - delta**0.5)/ (2*A)
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')
