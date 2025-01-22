larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
print('A Dimensão da Parede é de: {:.2f}m² '.format(area))
tinta = area / 2
print(f'Será necessários: {tinta:.2f} Lt de tinta, para pintar uma parede de: {area:.2f}m²')

#ALGORÍTMO DE DIMENSÕES DE UMA ÁREA E QUANTIDADE DE TINTA EM LITROS