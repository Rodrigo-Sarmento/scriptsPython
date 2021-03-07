from random import randint

n = randint(0,5)

resp = int(input('Qual número estou pensando de 0 a 5? '))

if resp == n:
    print('Acertou, pensei no número {}'.format(n))
else:
    print('Errou, pensei no número {}'.format(n))
