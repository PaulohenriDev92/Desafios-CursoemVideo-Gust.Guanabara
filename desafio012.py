
preco_produto = float(input('Valor do produto aqui: '))
desconto = 0.05 #valor do desconto em decimal, ou seja, 5%
valor_desconto = preco_produto * desconto
preco_final = preco_produto - valor_desconto
print(f'Valor Produto: {preco_produto:.2f} \nProduto já com Desconto: {preco_final:.2f}')

# ALGORÍTMO ACIMA FEITO C/ VARIÁVEIS

# ALGORÍTMO ABAIXO FEITO C/ VARIÁVEIS

"""
preco_produto = float(input('Valor Original: '))
desconto = preco_produto - (preco_produto * 5 / 100)
print('Valor original: R$ {:.2f} \nCom desconto de 5%: R$ {:.2f}'.format(preco_produto,  desconto))

"""