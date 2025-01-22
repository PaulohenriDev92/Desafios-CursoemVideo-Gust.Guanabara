nota1 = int(input('Digite a primeira nota: (0 - 100):  '))
nota2 = int(input('Digite a segunda nota: (0 - 100):  '))
media = (nota1 + nota2) / 2
if media >= 60:
    print(f'Sua Média foi: {media} APROVADO')    #CÁLCULO ARITMÉTICO - MÉDIA DE NOTAS DE ALUNO
elif media >= 50:
    print(f'Sua Média foi: {media} REPROVADO')
else:
    print(f'Sua Média foi: {media} RECUPERAÇÃO')