n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

numeros=(n1, n2, n3, n4)
pares=[]

print('Você digitou os valores {}'.format(numeros))
print('O valor {} apareceu {} vezes'.format(numeros[0],numeros.count(numeros[0])))
print('O valor {} apareceu na segunda posição'.format(numeros[1]))

for c in numeros:
    if c%2==0:
        pares.append(c)

print('Os valores pares digitados foram {}'.format(pares))
