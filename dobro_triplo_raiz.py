num = int (input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5  # no lugar do 0.5 pode-se usar o (1/2) OU pow(num,0.5) os dois elevam a potência de meio
print('O dobro de: {} é: {}'.format(num,dobro))
print('O triplo de: {} é: {}'.format(num,triplo))
print('A Raiz quadrada de: {} é: {:.2f}'.format(num,raiz_quadrada)) #ALGORÍTMO DE DOBRO/TRIPLO E RAIZ QUADRADA C/ VARIÁVEIS

"""
Elevando o número à potência de 0,5
O que significa?
Quando elevamos um número a uma potência, estamos multiplicando esse número por ele mesmo o número de vezes indicado 
pela potência. No caso de aumentar um número à potência de 0,5, estamos, na verdade, calculando a sua raiz quadrada.

Por que funciona?
A raiz quadrada de um número é o valor que, quando multiplicado por ele mesmo, resulta no número original. 
A operação de elevar um número à potência de 0,5 é a operação inversa da operação de elevar um número ao quadrado.
"""