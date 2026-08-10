# media e mediana

numeros = [int(x) for x in input().split()]

media = 0
mediana = 1
i = -max(numeros)
while media != mediana:
  numeros.append(i)
  numeros.sort()
  media = sum(numeros)/3
  mediana = numeros[1]
  numeros.remove(i)
  i += 1
else:
  print(i-1)
