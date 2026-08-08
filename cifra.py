# Cifra da Nlogônia (cifra.py)

palavraOriginal = input()
alfabeto = list('abcdefghijklmnopqrstuvwxyz')
vogais = list('aeiou')
consoantes = [x for x in alfabeto if x not in vogais]
resultado = ''

for i, char in enumerate(palavraOriginal):
  if char in vogais:
    resultado += char
    continue

  localAlfabeto = alfabeto.index(char)

  vogaisProximas = [abs(localAlfabeto - alfabeto.index(x)) for x in vogais]
  vogalProxima = vogais[vogaisProximas.index(min(vogaisProximas))]

  if char == 'z':
    consoanteProxima = 'z'
  else:
    consoanteProxima = consoantes[consoantes.index(char)+1]

  resultado += char + vogalProxima + consoanteProxima
print(resultado)
