import itertools

# Lendo a entrada
primeiraLinha = [int(x) for x in input().split()]
quantidadeIngredientes = primeiraLinha[0]
quantidadeIncompativeis = primeiraLinha[1]

# Armazenamos os incompatíveis como conjuntos (sets) de inteiros para buscas O(1)
incompativeis = []
for i in range(quantidadeIncompativeis):
    incompativeis.append(set(map(int, input().split())))

combinacoes_validas = 0

# Em vez de rodar um loop de 10^N, geramos diretamente as combinações de ingredientes.
# Iteramos sobre todos os tamanhos possíveis de sanduíche (de 1 a N ingredientes).
for tamanho in range(1, quantidadeIngredientes + 1):
    for comb in itertools.combinations(range(1, quantidadeIngredientes + 1), tamanho):
        comb_set = set(comb)
        
        # Checa se a combinação atual contém alguma combinação incompatível
        valida = True
        for inc in incompativeis:
            if inc.issubset(comb_set):
                valida = False
                break
        
        if valida:
            combinacoes_validas += 1

print(combinacoes_validas)