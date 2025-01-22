from datetime import date
ano_atual = date.today().year
nascimento = int (input('Ano de Nascimento: '))
idade = ano_atual - nascimento
print(f'Você nasceu em {nascimento} e tem {idade} anos em {ano_atual}')
if idade == 18:
    print('Se aliste IMEDIATAMENTE!')
elif idade < 18:
    tempo_falta = 18 - idade
    ano = ano_atual + tempo_falta
    print(f'Seu alistamento será em {ano}')
    print(f'Idade insuficiente para se alistar, pois possui {idade} anos, e ainda faltam {tempo_falta} anos')
elif idade > 18:
    tempo_passou = idade - 18
    ano = ano_atual - tempo_passou
    print(f'Seu alistamento foi em {ano}')
    print(f'Idade ultrapassada, pois vc tem {idade} e já passou {tempo_passou} anos de quando você tinha 18 anos')
