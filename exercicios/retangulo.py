quantidadeArvores = int(input())
intervalos = [int(x) for x in input().split()]

combinacoes = []

for i in range(len(intervalos)):
    combinacoes.append([])
    for j in range(len(intervalos)):
        if j == i:
            continue
        else:
            combinacoes[i].append(intervalos[i]+intervalos[j])

novasCombinacoes = []

for i in range(len(combinacoes)):
    for j in range(len(combinacoes[i])):
        if combinacoes[i][j] in intervalos:
            novasCombinacoes.append(combinacoes[i][j])

todosIntervalos = intervalos+novasCombinacoes

intervaloRepetidos = list(set([x for x in todosIntervalos if todosIntervalos.count(x) > 1]))

print(intervalos)
print(combinacoes)
print(novasCombinacoes)
print(todosIntervalos)
print(intervaloRepetidos)

if len(intervaloRepetidos) >= 2:
    print('S')
else:
    print('N')