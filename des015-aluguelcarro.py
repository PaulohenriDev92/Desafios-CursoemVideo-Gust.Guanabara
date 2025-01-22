try:
    diasAluguel = int(input('Quantos Dias Alugados ?'))
    kilorodados = float(input('Quantos Km rodados? '))
    percorridos = 60 * diasAluguel + 0.15 * kilorodados
    print(f'O total a pagar é de: R$ {percorridos} Reais \nPorque você Alugou: {diasAluguel} Dias e Percorreu: {kilorodados} KM')
except ValueError:
    print('Por favor digite apenas números')
#ALUGUEL DE CARRO
