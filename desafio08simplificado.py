m = float (input('Digite aqui a quantidade em metros: '))
print('O valor em Centímetros é de: {}cm \nMilímetros é: {}mm \nQuilômetros é de: {:.3f}km \nHectômetros é de: {}hm \nDecâmetro é de: {:.1f}dam \nDecímetro é de: {:.0f}dm'
      .format((m * 100), (m * 1000), (m * 0.001), (m * 0.01), (m * 0.1), (m * 10)))

# CONVERSOR DE MEDIDAS SEM VARIÁVEIS