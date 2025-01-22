
pre_produto = float(input(' Digite o valor do produto aqui: '))
desconto_avista = pre_produto - (pre_produto * 10 / 100)
desconto_aprazo = pre_produto - (pre_produto * 5 / 100)
print(f'O Preço deste produto à vista fica de: {desconto_avista:.2f}\nO preço deste produto à prazo fica de: {desconto_aprazo:.2f}')

#ALGORÍTMO PARA SABER SE A PESSOA É MENOR DE IDADE
"""
try:
    anos = int(input('Digite aqui sua idade: '))
    if anos >=18:
        print(f'Parabéns você é maior de idade. Porque você tem: {anos} anos')
    else:
        print(f'Você é menor de idade, pois tem apenas: {anos} anos')
except ValueError:
    print('Por favor digite apenas números')
    
"""