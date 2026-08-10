# Plano de Internet
xPadrao = int(input())  # Usada como constante para comparar os valores
n = int(input())
xAdd = 0
xAdd += xPadrao         # cria uma cópia do X que será alteravel


meses = []
for i in range(n):
  m_i = int(input())
  meses.append(m_i)
  xAdd = xPadrao + (xAdd - meses[i])
print(xAdd)
