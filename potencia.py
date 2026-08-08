# Potência (potencia.py)
quantidadeOp = int(input())
resultado = 0
for i in range(quantidadeOp):
  operacao = list(input())
  potencia = int(operacao.pop(-1))
  resultado += int("".join(operacao))**potencia

print(resultado)
