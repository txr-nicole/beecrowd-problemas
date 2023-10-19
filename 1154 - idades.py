soma = 0
count = 0
while True:
    num = int(input())
    if num <= 0:
        break
    else:
        soma += num
        count += 1
media = soma / count
print(f"{media:.2f}")
