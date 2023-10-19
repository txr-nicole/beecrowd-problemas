casos = int(input())
count = 0
while count < casos:
    nivel = int(input())
    if nivel > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")
    count += 1
