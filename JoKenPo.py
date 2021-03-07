from random import randint
from time import sleep

print(""" Suas opções:
            [ 0 ] PEDRA
            [ 1 ] PAPEL
            [ 2 ] TESOURA""")

usuario = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')

computador = (randint(0,2))

print('-=-'*8)

if usuario ==0 and computador ==0:
    print(' Computador jogou PEDRA \n Jogador jogou PEDRA \n EMPATE!')
elif usuario ==0 and computador ==1:
    print(' Computador jogou PAPEL \n Jogador jogou PEDRA \n COMPUTADOR VENCE')
elif usuario ==0 and computador ==2:
    print(' Computador jogou TESOURA \n Jogador jogou PEDRA \n JOGADOR VENCE')
elif usuario ==1 and computador ==0:
    print(' Computador jogou PEDRA \n Jogador jogou PAPEL \n JOGADOR VENCE')
elif usuario ==1 and computador ==1:
    print(' Computador jogou PAPEL \n Jogador jogou PAPEL \n EMPATE!')
elif usuario ==1 and computador ==2:
    print(' Computador jogou TESOURA \n Jogador jogou PAPEL \n COMPUTADOR VENCE')
elif usuario ==2 and computador ==0:
    print(' Computador jogou PEDRA \n Jogador jogou TESOURA \n COMPUTADOR VENCE')
elif usuario ==2 and computador ==1:
    print(' Computador jogou PAPEL \n Jogador jogou TESOURA \n JOGADOR VENCE')
elif usuario ==2 and computador ==2:
    print(' Computador jogou TESOURA \n Jogador jogou TESOURA \n EMPATE!!')
else:
    print('ERRO!')

print('-=-'*8)
