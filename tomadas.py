# # Tomadas
# tomadasInput = input()
# tomadas = sorted(list(map(int, tomadasInput.split())), reverse=True)
# contador = 0

# for i in range(len(tomadas)): # encontrei uma formula pra resolver
#   contador += tomadas[i]-1

# print(contador+1)

# # Dá até para facilitar mais ainda com a formula
tomadasInput = input()
tomadas = list(map(int, tomadasInput.split()))

print(sum(tomadas)-3)

# # Com recurção em vez da fórmula
# tomadasInput = input()
# tomadas = sorted(list(map(int, tomadasInput.split())), reverse=True)

# contador = 0

# def contar_tomadas(reguas):
#   global contador
#   if reguas[0] >= (len(reguas)-1):
#     return (reguas[0]-(len(reguas)-1)) + sum(reguas[1:]) + contador
#   else:
#     contador += reguas[0]-1
#     return contar_tomadas(reguas[1:])

# print(contar_tomadas(tomadas))
