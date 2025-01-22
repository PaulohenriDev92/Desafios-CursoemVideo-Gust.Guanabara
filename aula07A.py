n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2                               # {:.3f}  deixa apenas 3 casas decimais após o ponto. chamado de ponto flutuante
d = n1/n2                               # , end=' '  usa-se para dar continuidade na mesma linha, sem pular
di = n1//n2                             # \n  significa nova linha
exp= n1**n2
print('A soma é: {},\nA multiplicação é: {},\ne a Divisão é: {:.3f} '.format(s,m,d), end='. ')
print('Tendo como a Divisão Inteira: {} , e a Exponenciação: {} '.format(di,exp))

