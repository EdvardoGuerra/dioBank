menu = """
 
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair
 
 =>  """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao =='d':
        print('Depósito')
        print('-' * 20)
        while True:
            deposito =input('Qual o valor a depositar? ')
            deposito = float(deposito)
            if deposito >= 0:
                saldo += deposito
                extrato += f'Depósito: R${deposito:.2f}\n'
                break
            else:
                print('O valor deve ser positivo. Tente novamente.')
                break
    elif opcao =='s':
        print('Saque')
        print('-' * 20)
        while True:
            saque = input('Qual o valor a sacar? ')
            saque = float(saque)
            if saque > limite:
                print(f'O valor máximo de saque é de R${limite:.2f}')
                break
            elif (0 < saque <= limite) and (saque <= saldo) and (numero_saques < LIMITE_SAQUES):
                saldo -= saque
                extrato += f'Saque: R${saque:.2f}\n'
                numero_saques += 1
                break
            elif saque > saldo:
                print('Saldo insuficiente. Tente novamente.')
                break
            elif numero_saques >= LIMITE_SAQUES:
                print('Limite máximo de saques por dia foi excedido. Tente novamente em outro dia.')
                break
            elif saque < 0:
                print('O valor deve ser positivo. Tente novamente.')
                break
    elif opcao=='e':
        print('Extrato')
        print('-' * 20)
        print(extrato)
        print(f'Saldo: R${saldo:.2f}\n')
    elif opcao=='q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada. ')
    
 