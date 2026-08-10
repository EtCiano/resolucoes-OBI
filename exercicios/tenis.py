amigos = []
for i in range(4):
    amigos.append(int(input()))
    
amigos.sort()
diferenca = (amigos[0]+amigos[3]) - (amigos[1]+amigos[2])
print(diferenca)