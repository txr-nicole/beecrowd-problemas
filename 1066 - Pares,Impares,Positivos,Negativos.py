count = 0
par = 0
impar = 0
pos = 0
neg = 0
while count < 5:
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    count += 1
print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")
