# Sistema de banco
from time import sleep
from colorama import init,Fore
init(autoreset=True)
import random

# LOGIN
print(Fore.GREEN + '-=-' * 20 + 'BANCO PYTHON(LOGIN)' + '-=-' * 20)
extrato = []
saldo = float(input('Qual o seu saldo atual?'))# Definição do saldo
senha_criada = str(input('Crie sua senha:')) # Definição da senha
tentativas_atuais = 0
tentativas_maximas = 3
logado = False # O padrão é falso
while tentativas_atuais < tentativas_maximas: # Inicia o loop para a senha.
    print('Confirme sua senha para acessar sua conta...')
    sleep(2)
    palpite = str(input('Digite a senha:'))
    if palpite == senha_criada:
        print(Fore.GREEN +'LOGIN REALIZADO COM SUCESSO!')
        logado = True
        break #Encerra o loop caso acerte a senha.
    else:
        tentativas_atuais += 1
        print(f'SENHA INCORRETA! Ainda restam {tentativas_maximas - tentativas_atuais} tentativas.')
if tentativas_atuais == tentativas_maximas:
    print('ACESSO BLOQUEADO! PROCURE O ADMINISTRADOR.')

# Operações bancárias
if logado:
    print(Fore.BLUE+'ACESSANDO SUA CONTA...')
    sleep(1)
    while True:
        sleep(1)
        print(Fore.GREEN + '-=-' * 20 + 'MENU PRINCIPAL' + '-=-' * 20)
        print(Fore.GREEN+'[1] Ver Saldo')
        print(Fore.GREEN+'[2] Sacar')
        print(Fore.GREEN+'[3] Depositar')
        print(Fore.RED+'[4] Sair')
        print(Fore.GREEN + '[5] Ver extrato')
        opcao = str(input('Escolha uma opção:'))
        if opcao == '1':
            print(f'{Fore.GREEN}Seu saldo atual é: R${saldo:.2f}')
        elif opcao == '2':
            try:
                taxa = 2.50
                valor = float(input('Quanto deseja sacar?R$'))
                if valor > 500:
                    print(Fore.RED+'Limite máximo por saque é de R$ 500.00')
                elif valor + taxa > saldo:
                    print(Fore.RED+'Saldo insuficiente para saque + taxa de R$ 2.50')
                else:
                    saldo -= (valor + taxa)
                    extrato.append(f'Saque: -{valor:.2f}(Taxa: R$ 2.50)')
                    print(Fore.GREEN+ f'Saque realizado com sucesso!Taxa de R$ 2.50 aplicada.')
            except ValueError:
                print(Fore.RED + "Erro: Por favor, digite um valor numérico válido.")
        elif opcao == '3':
            try:
                deposito = float(input('Quanto deseja depositar?R$'))
                saldo += deposito
                extrato.append(f'Depósito: +{deposito:.2f}')
                print(f'{Fore.GREEN}Depósito de R${deposito:.2f} realizado com sucesso!Novo saldo: {saldo:.2f}')
            except ValueError:
                print(Fore.RED + 'Erro! Digite um valor numérico.')
        elif opcao == '5':
            print(Fore.CYAN + '-=-'*20 + 'EXTRATO BANCÁRIO' + '-=-'*20)
            # Se a lista estiver vazia avisamos ao usuário
            if len(extrato) == 0:
                print(Fore.RED + 'NENHUMA TRANSAÇÃO REALIZADA!')
            # Mostra a lista de extrato
            else:
                for transacao in extrato:
                    print(Fore.WHITE + transacao)
        elif opcao == '4':
            sleep(1)
            print(f'{Fore.CYAN}Obrigado por usar o Banco python! Volte sempre!')
            break
        else:
            print('Opção inválida!')
            input(f'{Fore.YELLOW}Pressione enter para voltar ao menu')