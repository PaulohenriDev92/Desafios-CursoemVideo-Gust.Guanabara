print('-=-' * 15)
print(' ' * 4, 'PROGRAMA DE BASE DE CONVERSÃO', ' ' * 4)
print('-=-' * 15)
num = int (input('Digite um número inteiro: '))
print ('''
1 - CONVERSÃO PARA BINÁRIO
2 - CONVERSÃO PARA OCTAL
3 - CONVERSÃO PARA HEXADECIMAL
''')
print('-=-' * 15)
op = int (input('Escolha uma opção para conversão: '))
if op == 1:
    print(f'{num} Convertido para BINÁRIO fica {bin(num)[2:]}')
elif op == 2:
    print(f'{num} Convertido para OCTAL fica {oct(num)[2:]}')
elif op == 3:
    print(f'{num} Convertido para HEXADECIMAL fica {hex(num)[2:]}')
else:
    print(f'Opção INVÁLIDA')
