def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat

while True:
    try:
        n1, n2 = map(int, input().split())
        fatN1 = fatorial(n1)
        fatN2 = fatorial(n2)
        soma = fatN1 + fatN2
        print(soma)

    except EOFError:
        break
