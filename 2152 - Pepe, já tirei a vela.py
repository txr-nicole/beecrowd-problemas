qtde = int(input())
cont = 0
while cont < qtde:
    cont += 1
    H,M,O = input().split()
    if len(H) == 1:
        H = "0"+ H
    if len(M) == 1:
        M = "0"+ M
    print(f'{H}:{M}',end="")
    if O == "1":
        print(' - A porta abriu!')
    else:
        print(' - A porta fechou!')
