A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
numeros = [A,B,C,D,E]
pares = 0
for numero in numeros:
    if (numero % 2 == 0):
        pares += 1
print(f'{pares} valores pares')
