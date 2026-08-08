#Zero para cancelar
quant = int(input())

numeros = []
for i in range(quant):
    numero = int(input())

    if numero! = 0 :
        numeros.append(numero)
    else:
        numeros.pop()

print(sum(numeros))
