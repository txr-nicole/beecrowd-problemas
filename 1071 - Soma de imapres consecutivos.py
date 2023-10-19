def impar(n):
    return n % 2 != 0
x = int(input())
y = int(input())

if x > y:
    temp = x
    x = y
    y = temp
    
n = x + 1
soma = 0

while n < y:
    if impar(n):
        soma += n
    n+=1
print(soma)

