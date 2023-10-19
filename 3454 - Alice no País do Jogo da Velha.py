jogo = input()
if(jogo[0] == "X" and jogo[1] == "X" and jogo[2] == "O") or (jogo[0] == "O" and jogo[1] == "X" and jogo[2] == "X"):
    print("Alice")
elif (jogo[0] == "X" and jogo[2] == "X" and jogo[1] == "O"):
    print("*")
else:
    print("?")

