# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#Programa escrito como atividade do bootcampo "Potência Tech powered by iFood | Ciências de Dados com Python", ministrado Digital Innovation One - DIO.
#Programa escrito em compilador online "https://www.programiz.com/python-programming/online-compiler"


menu = '''

===============================================
----- Seja bem vindo ao Sistema Bancário -----
===============================================

---- Digite o número da operação desejada ----

[1] - Saque\n[2] - Depositar\n[3] - Visualizar Extrato\n[0] - Sair\n

'''

saldo = int(0)
limite = 500
extrato = "Detalhes\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Qual o valor do saque? "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
    
        elif excedeu_limite:
            print("Operação falhou! Limite diário excedido")
    
        elif excedeu_saques:
            print("Operação falhou! Limite de saques diários excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
        else:
         print("Falha na operação! O valor informado é inválido.")
        
        
    elif opcao == "2":
        valor = float(input("Informe o valor depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Falha na operação! O valor informado é inválido.")
    
    elif opcao == "3":
        
        print("------ Extrato ------\n")
        print("Não há registro de movimentações." if not extrato else extrato)
        print(f"\n Saldo atual: R$ {saldo:.2f}")
        print("========================")
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida! Por gentileza, selecione uma das opções disponíveis")
        
    