# Cubo e quadrado (cubo.py)
import math
primeiroNum = int(input())
segundoNum = int(input())
contagem = 0
for i in range(primeiroNum, segundoNum + 1):
  if (f"{math.cbrt(i):.2f}"[-1] == '0' and f"{math.cbrt(i):.2f}"[-2] == '0') and (f"{math.sqrt(i):.2f}"[-1] == '0' and f"{math.sqrt(i):.2f}"[-2] == '0'):
    contagem += 1
print(contagem)
