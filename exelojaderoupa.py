
print(f'{'-' * 18} {'LOJA DE ROUPAS DO PAULO'} {'-' * 18}')
nCamisas = int(input('Quantidade de Camisas: '))
vCamisas = 14.75
vFinal = nCamisas * vCamisas
if nCamisas <= 5:
    vFinal = vFinal * (1 - 3/100)
elif nCamisas <= 10:
        vFinal = vFinal * (1 - 5/100)
else:
    vFinal = vFinal * (1 - 7/100)
print(f'O valor final foi de: R$ {vFinal:.2f}')
