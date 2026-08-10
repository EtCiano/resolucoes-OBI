# Três por dois (3por2.py)
quantidade = int(input())
chocolates = []
for i in range(quantidade):
  chocolates.append(int(input()))
chocolates.sort(reverse=True)
subgrupos = []
for i in range(len(chocolates)//3):
  subgrupos.append([chocolates.pop(), chocolates.pop(), chocolates.pop()])
subgrupos.append(chocolates)
chocolates = []
soma = 0
for subgrupo in subgrupos:
  subgrupo.sort(reverse=True)
  for i, chocolate in enumerate(subgrupo):
    if i == 2:
      continue
    else:
      soma += chocolate
print(soma)
