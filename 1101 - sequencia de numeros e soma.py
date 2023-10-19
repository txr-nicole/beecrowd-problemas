while True:
    M , N = list(map(int, input().split()))
    if N > M:
        temp = N
        N = M
        M = temp
    soma = 0
    if (M == 0 or M < 0) or (N == 0 or N < 0):  break
    else:
        for i in range(N,M+1):
            soma += i
            print(i, end=" ")
    print(f"Sum={soma}")
            
