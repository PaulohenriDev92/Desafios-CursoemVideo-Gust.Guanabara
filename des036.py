casa = float (input('Valor da casa: '))
salario = float (input('Valor do salário: '))
anos = int (input('Quantidade de anos do financiamento: '))
# Calcula o número total de meses do financiamento e divide o valor da casa para obter a prestação mensal
prestacao  = casa / (anos * 12)
# Calcula o valor máximo da prestação, que é 30% do salário
minimo = salario * 30 / 100
# Condição: se a prestação calculada for menor ou igual ao valor mínimo permitido
if prestacao <= minimo:
    print(f'DEFERIDO o empréstimo, a prestação será de {prestacao:.2f}', end = '')
else:
    print(f'INDEFERIO o empréstimo, vocÊ ultrapassou os 30% do valor do limite do seu salário que foi de {minimo:.2f} ')