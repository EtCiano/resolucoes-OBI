# Baldes
linha1 = input()
quantBaldes = int(linha1.split(' ')[0])
quantOperacoes = int(linha1.split(' ')[1])
linha2 = input().split(' ')
bolas = {int(x): linha2.index(x) for x in linha2}
diferencas = []
maior = 0
menor = 0
for i in range(quantOperacoes):
  linha = input()
  if linha[0] == '1':
    opAdicionar = [int(x) for x in linha.split(' ')]
    opAdicionar.pop(0)
    opAdicionar[1] -= 1
    bolas[opAdicionar[0]] = opAdicionar[1]
  else:
    intervalo = range(linha[1]-1, linha[2])

for peso, balde in bolas.itens():
  pass

print(bolas)
