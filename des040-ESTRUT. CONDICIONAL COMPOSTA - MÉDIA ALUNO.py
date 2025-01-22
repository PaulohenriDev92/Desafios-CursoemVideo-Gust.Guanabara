import datetime
import emoji
data_atual = datetime.datetime.now()
print('-=-' * 5, ' NOTAS DOS ALUNOS', '-=-' * 5)
data_formatada = data_atual.strftime('%Y-%m-%d' ' às ' '%H:%M')
print(f'{'':>7}Data atualizada: {data_formatada}')
print('-=-' * 3, 'MÉDIA DAS NOTAS LOGO ABAIXO','-=-' * 4, end='\n\n')
nota1 = float (input('Qual a PRIMEIRA nota: '))
nota2 = float (input('Qual a SEGUNDA nota: '))
soma_media = (nota1 + nota2) / 2
if soma_media < 5:
    print(f'Aluno REPROVADO, tirou média: {soma_media}. Sinto muito \U0001F622\U0001F44E', end='\n\n')
elif 5 <= soma_media < 6.9:
    print(f'Aluno em RECUPERAÇÃO, tirou média: {soma_media:.1f} \U0001F622\U0001F44E', end='\n\n')
elif soma_media >= 7:
    print(f'Aluno APROVADO, tirou média: {soma_media}. Parabéns \U0001F600\U0001F44D ', end='\n\n')
print('-=-'  * 5, 'FIM DO PROGRAMA', '-=-' * 7)

