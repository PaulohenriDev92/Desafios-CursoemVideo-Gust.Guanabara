print(f'{'#' * 18} {'GRANDEZAS ELÉTRICAS'} {'#' * 18}')
print('1. Tensão (em Volts) ')
print('2. Resistência (em Ohm) ')
print('3. Corrente (em Ampére) ')
print('#' * 58)
op = int(input('Qual grandeza deseja calcular? '))
if op < 1 or op > 3:
    print('Opção Inválida')
elif op == 1:
    R = float(input('Digite o valor da corrente (em Ohm): '))
    i = float(input('Digite o valor da corrente (em Ampére): '))
    V = R * i
    print(f'\nV = {V:.2F}')
elif op == 2:
    V = float(input('Digite o valor da corrente (em Volts): '))
    i = float(input('Digite o valor da corrente (em Ampére): '))
    R = V / i
    print(f'\nR = {R:.2f}')
else:
    V = float(input('Digite o valor da corrente (em Volts): '))
    R = float(input('Digite o valor da corrente (em Ohm): '))
    i = V / R
    print(f'\ni = {i:.2f}')