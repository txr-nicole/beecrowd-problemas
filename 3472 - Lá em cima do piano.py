def flavio_josephus(n, k):
    posicao = 0
    
    # Criando uma lista com as pessoas
    pessoas = list(range(1, n+1))
    
    while len(pessoas) > 1:
        # Calculando a próxima posição a ser eliminada
        posicao = (posicao + k - 1) % len(pessoas)
        
        # Removendo a pessoa da lista
        pessoas.pop(posicao)
    
    # A última pessoa que sobrou
    return pessoas[0]
nPessoas = int(input())
contagem = 29
if flavio_josephus(nPessoas, contagem) == 1:
    print("vai ganhar")
else:
    print("nao vai ganhar")
