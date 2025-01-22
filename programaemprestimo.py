print('$$ BANCO EMPRÉSTIMOS DO BRASIL $$ (Digite: 1 - SIM e 0 - NÃO)')
nomeRestrito = int(input(' Seu nome está sujo? '))
if nomeRestrito == 1:
    print('INFELIZMENTE NÃO CONSEGUIREMOS LIBERAR SEU EMPRÉSTIMO AGORA')
else:
    possuiTrabalho = int(input('Está empregado com carteira Assinada? '))
    if possuiTrabalho == 0:
        print('INFELIZMENTE NÃO CONSEGUIREMOS LIBERAR SEU EMPRÉSTIMO AGORA')
    else:
         temCasa = int(input('Possui casa própria? '))
         if temCasa == 0:
             print('INFELIZMENTE NÃO CONSEGUIREMOS LIBERAR SEU EMPRÉSTIMO AGORA')
         else:
             print('EMPRÉSTIMO AUTORIZADO')
