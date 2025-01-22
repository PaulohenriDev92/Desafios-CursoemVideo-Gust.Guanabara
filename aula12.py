nome = str (input('Whats is your name? ')).strip()
if nome == 'Paulo'.upper():
    print(f'Que nome Lindo \033[31m{nome}\033[m')                 # ESTRUTURAS ANINHADAS
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Alexandre':
    print(f'Seu nome é bastante popular no Brasil \033[33m{nome}\033[m')
elif nome in 'Ana' 'Paula' 'julia' 'Ricarda':
    print(f'Que belo nome Feminino {nome}')
else:
    print(f'Seu nome é normal {nome}')
print(f'Boa Noite \033[31m{nome}\033[m')