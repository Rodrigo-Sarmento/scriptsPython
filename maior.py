def maior(* num):
    maior = 0
    for valor in num:
        if valor >= maior:
            maior = valor
    print(f'{num}Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(1,2,3,4,5)
