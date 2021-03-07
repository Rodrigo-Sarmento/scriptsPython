num = int(input('Digite um inteiro:'))

print('Escolha uma das bases para conversão: \n [ 1 ] converter para BINÁRIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter para hexadecimal')

opcao = int(input('Sua opção: '))

if opcao ==1:
    bi = format(num, "b")
    print('{} convertido para BINÁRIO é igual: {}'.format(num, bi))
elif opcao ==2:
    oc = format(num, "o")
    print('{} convertido para OCTAL é igual: {}'.format(num, oc))
elif opcao == 3:
    he = format(num, "x")
    print('{} convertido para HEXADECIMAL é igual: {}'.format(num, he))
else:
    print('ERRO!')
