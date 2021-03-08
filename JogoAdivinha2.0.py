from random import randint

print('Pensei em um número entre 0 e 10, tente adivinhar!')

num = randint(0,10)
c=0
final = 0
while final == 0:
    tent = int(input('Qual número eu pensei?'))
    c+=1
    if tent == num:
        print('Parabéns você acertou com {} tentativas \n o número era {}'.format(c, num))
        final = 1
