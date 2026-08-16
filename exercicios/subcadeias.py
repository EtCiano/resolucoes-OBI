comprimento= int(input())
cadeia = input()

subcadeias = []

for i in range(1, comprimento+1):
    for j in range((comprimento+1)-i):
        subcadeias.append(cadeia[j:j+i])

print(max([len(x) for x in subcadeias if x == x[::-1]]))

