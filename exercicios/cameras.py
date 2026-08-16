cameras = []

primeiraLinha = [int(x) for x in input().split()]

digitos = {
    'vazio': '.',
    'naoVisto': '*',
    'visto': '#'
}

tamanho = {
    'x': primeiraLinha[0],
    'y': primeiraLinha[1]
    }

tela = []

for y in range(tamanho['y']):
    tela.append([])
    for x in range(tamanho['x']):
        tela[-1].append(digitos['vazio'])

tela[0][0] = digitos['naoVisto']

entrada = {
    'x': 0,
    'y': 0
    }

saida = {
    'x': tamanho['x']-1, 
    'y': tamanho['y']-1
    }

quantCam = primeiraLinha[2]

for i in range(quantCam):
    linha = input().split()
    cameras.append({
        'x': int(linha[0])-1,
        'y': int(linha[1])-1,
        'direcao': linha[2],
        'areasCobertas': []
        })

    quantidadeCelulas = 0
    colunasCobertas = []
    linhasCobertas = []
    
    match cameras[-1]['direcao']:
        case 'N':
            quantidadeCelulas = tamanho['y']-(saida['y'] - cameras[-1]['y'])

            colunasCobertas.extend([cameras[-1]['x']] * quantidadeCelulas)
            linhasCobertas = list(range(0, cameras[-1]['y']+1))

        case 'L':
            quantidadeCelulas = tamanho['x']-(cameras[-1]['x'])

            colunasCobertas = list(range(cameras[-1]['x'], tamanho['x']))
            linhasCobertas.extend([cameras[-1]['y']] * quantidadeCelulas)

        case 'S':
            quantidadeCelulas = tamanho['y']-(cameras[-1]['y'])

            colunasCobertas.extend([cameras[-1]['x']] * quantidadeCelulas)
            linhasCobertas = list(range(cameras[-1]['y'], tamanho['y']))

        case 'O':
            quantidadeCelulas = tamanho['x']-(saida['x'] - cameras[-1]['x'])

            colunasCobertas = list(range(0, cameras[-1]['x']+1))
            linhasCobertas.extend([cameras[-1]['y']] * quantidadeCelulas)

    for i in range(quantidadeCelulas):
        cameras[-1]['areasCobertas'].append({'x': colunasCobertas[i], 'y': linhasCobertas[i]})
        tela[linhasCobertas[i]][colunasCobertas[i]] = digitos['visto']

def preencherTela(y, x):
    global tela

    if tela[y][x] == digitos['vazio']:
        return

    if tela[y][x] == digitos['naoVisto']:

        if y > 0:
            if tela[y-1][x] == digitos['vazio']:
                tela[y-1][x] = digitos['naoVisto']
                preencherTela(y-1, x)
        if y < tamanho['y']-1:
            if tela[y+1][x] == digitos['vazio']:
                tela[y+1][x] = digitos['naoVisto']
                preencherTela(y+1, x)

        if x > 0:
            if tela[y][x-1] == digitos['vazio']:
                tela[y][x-1] = digitos['naoVisto']
                preencherTela(y, x-1)
        if x < tamanho['x']-1:
            if tela[y][x+1] == digitos['vazio']:
                tela[y][x+1] = digitos['naoVisto']
                preencherTela(y, x+1)

    if tela[y][x] == digitos['visto']:
        return


preencherTela(0, 0)

if tela[saida['y']][saida['x']] == digitos['naoVisto']:
    print('S')
elif tela[saida['y']][saida['x']] == digitos['vazio']:
    print('N')