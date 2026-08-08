# Cálculo rápido
s = int(input())
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
  digitos = list(str(i))
  digitos = [int(x) for x in digitos]
  if sum(digitos) == s:
    count += 1
print(count)
