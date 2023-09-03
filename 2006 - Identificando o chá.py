T = int(input())
entrada = input().split()
respostas = list(map(int, entrada))
acertos = 0
for chute in respostas:
    if chute == T:
        acertos += 1
print(acertos)
