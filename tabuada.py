n = int(input('Digite o número que você deseja saber a tabuada: '))

for c in range(0,11):
    result = n*c
    print('{} X {} = {}'.format(n, c, result))
