m = float(input('Digite aqui a quantidade de metros: '))
cent = m * 100
mili = m * 1000
km = m * 0.001
hm = m * 0.01
dca = m * 0.1
dci =  m * 10
print('Centímetros é de: {}cm\nMilímetros é: {}mm \nQuilômetros é: {:.3f}km \nHectômetro é: {:.2f}hm \nDecâmetro é: {:.1f}dam \nDecímetro é: {:.0f}dm '
      .format(cent, mili, km, hm, dca, dci ))
# CONVERSOR DE MEDIDAS COM VARIÁVEIS