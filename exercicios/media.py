# media e mediana
a = int(input())
b = int(input())

media = 0
mediana = 1
numeros = [a, b]
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
