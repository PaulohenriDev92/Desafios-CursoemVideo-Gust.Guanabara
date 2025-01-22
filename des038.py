n1 = int (input('Primeiro número: '))
n2 = int (input('Segundo número: '))
if n1 > n2:
    print('O \033[31mPRIMEIRO\033[m valor é \033[31mMAIOR')
elif n2 > n1:
    print('O \033[32mSEGUNDO\033[m valor é \033[32mMAIOR')
else:
    print('Os \033[33mDOIS\033[m valores são \033[33mIGUAIS')