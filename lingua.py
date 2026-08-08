# Língua do P (lingua.py)

frase = list(input())
resultado = [x for x in frase if x != 'p']
print(''.join(resultado))
