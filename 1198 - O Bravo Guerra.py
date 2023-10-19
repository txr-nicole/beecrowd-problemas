while True:
    try:
        possui, oponentes = map(int, input().split())
        diferenca = oponentes - possui
        print(abs(diferenca))
    except EOFError:
        break
