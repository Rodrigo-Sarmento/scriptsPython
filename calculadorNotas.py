nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = ((nota1 + nota2)/2)

if(media>=7):
    print('sua média foi: {:.2f}'.format(media))
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
    print('sua média foi: {:.2f}'.format(media))
        
