import time

# 1. Variáveis iniciais
saldo = 1000.00
historico = []

print('🏧  --- Bem-vindo ao Caixa Eletrônico ---')

# 2. Laço principal que mantém o programa em execução
while True:
    print('''\n --- Menu Principal ---
          [1] - Depositar
          [2] - Sacar
          [3] - Ver Saldo
          [4] - Ver Histórico
          [5] - Sair
          ''')
    
    opcao = input('➡️  Escolha uma opção: ')
    
    # Lógica para a opção de Depósito
    if opcao == '1':
        valor_deposito = float(input('➡️  Digite o valor para depósito: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            registro = f'Depósito: +R$ {valor_deposito:.2f}'
            historico.append(registro)
            print('✅  Depósito realizado com sucesso.')
        else: 
            print('❌  Valor inválido. O depósito deve ser um número positivo.')
            
    # Lógica para a opção de Saque
    elif opcao == '2':
        valor_saque = float(input('➡️  Digite o valor para Saque: '))
        # Validação condicional
        if valor_saque <= 0:
            print('❌  Valor inválido! O saque deve ser um número positivo.')
        elif valor_saque > saldo:
            print('❌  Saldo insuficiente para realizar este saque.')
        else:
            saldo -= valor_saque
            registro = f'Saque: -R$ {valor_saque:.2f}'
            historico.append(registro)
            print('✅  Saque realizado com sucesso! Retire o dinheiro.')
            
    # Lógica para ver o Saldo
    elif opcao == '3':
        print(f'💰  Seu saldo atual é: R$ {saldo:.2f}')

    # Lógica para ver o Histórico
    elif opcao == '4':
        print('🗺️ --- Histórico de Transações ---')
        if not historico: # Verifica se a lista está vazia
            print('❌ Nehuma transação foi realizada ainda.')
        else: 
            for transacao in historico:
                print(transacao)
                
    # Lógica para sair
    elif opcao == '5':
        print('📤  Obrigado por utilizar nosso caixa eletrônico. Finalizando...')
        time.sleep(1) # Pequena pausa
        break # Encerra o laço while
    
    # Lógica para opção inválida
    else: 
        print('❌  Opção inválida. Por favor, escolha uma das opções do menu.')