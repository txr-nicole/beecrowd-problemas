inicio,iMinutos,fim,fMinutos = map(int,input().split())

duracao = inicio*60 + iMinutos
Dfim = fim*60 + fMinutos

if duracao < Dfim: tempo = Dfim - duracao
elif fim < duracao: tempo = ((24*60) - duracao) + Dfim
elif duracao == Dfim: tempo = (24*60)

hora = tempo // 60
minuto = tempo % 60

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
