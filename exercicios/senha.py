# senha da vo zinha
primeiraLinha = [int(x) for x in input().split()]

caracteresSenha = primeiraLinha[0]
letrasBorradas = primeiraLinha[1]
comprimentoPalavras = primeiraLinha[2]

senha = input()

palavras = []

for i in range(letrasBorradas):
  palavras.append(input())

indexSenha = int(input())-1

def passarPorPalavra(palavra):
  global palavras

  palavraFinal = []

  for i, letra in enumerate(palavra):

    if palavras[-1] == palavra:
      palavraFinal.append(letra)

    else:
      
      letrasSeguintes = passarPorPalavra(palavras[palavras.index(palavra)+1])
      for secLetras in letrasSeguintes:
        palavraFinal.append(letra+secLetras)

  return palavraFinal


combinacoes = passarPorPalavra(palavras[0])

senhas = []

for combinacao in combinacoes:
  senhaAdicionar = senha
  for letra in combinacao:
    senhaAdicionar = senhaAdicionar.replace('#', letra, 1)

  senhas.append(senhaAdicionar)

senhas.sort()

print(senhas[indexSenha])