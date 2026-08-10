primeiraLinha = [int(x) for x in input().split()]
quantidadeEstacoes = primeiraLinha[0]
quantidadeComandos = primeiraLinha[1]
estacaoDevastada   = primeiraLinha[2]

comandos = [int(x) for x in input().split()]

estacaoAtual = 1 # inicia na 1
contagemDevastacao = 0

print(estacaoAtual)
for comando in comandos:
    if estacaoAtual == estacaoDevastada:
            contagemDevastacao += 1
    estacaoAtual += comando
    print(estacaoAtual)
    if estacaoAtual <= 0:
        estacaoAtual = quantidadeEstacoes
        
if estacaoAtual == estacaoDevastada:
    contagemDevastacao += 1

print(contagemDevastacao)
