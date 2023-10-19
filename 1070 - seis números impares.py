def impar(n):
    return n % 2 != 0

num = int(input())
cont = 0
while cont < 6:
    if impar(num):
        print(num)
        cont += 1
    num += 1
    
    
    
