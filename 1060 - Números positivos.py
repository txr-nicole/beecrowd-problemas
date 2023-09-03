A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())
numeros = [A,B,C,D,E,F]
positivos = 0
for numero in numeros:
    if (numero > 0):
        positivos += 1
print(f'{positivos} valores positivos')
