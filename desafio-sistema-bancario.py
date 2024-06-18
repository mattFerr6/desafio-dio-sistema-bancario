import os
import time


def limparTela():
    os.system('cls')


def loading():
    time.sleep(4)


menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

==>  """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
primeiro_acesso = 1

while True:
    if not primeiro_acesso:
        loading()
    else:
        primeiro_acesso = 0
    
    limparTela()

    opcao = int(input(menu))

    if opcao == 0:
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito
            numero_saques += 1
        else:
            print("Valor inválido.")
        deposito = 0
        print("Depósito efetuado com sucesso.")

    elif opcao == 1:
        if numero_saques <= LIMITE_SAQUES:
            print("Fique atento! Limite de R$500,00 por saque.")
            valor_saque = float(input("Digite o valor para saque:"))
            if valor_saque > 0 and valor_saque < 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print(f"""
Saque efetuado.
Valor do saque: R${valor_saque:.2f}
""")                
                    extrato.append(f"""Saque efetuado.
Data: 01/01/2022
Hora: 00:00
Valor: R${valor_saque:.2f}""")
                    numero_saques += 1
                else:
                    print("Valor insuficiente.")
            else:
                print("Valor de saque inválido. Limite de R$500,00 por saque.")
            valor_saque = 0
        else:
            print("Limite diário de saque atingido. Tente novamente dentro de 24h")
        

    elif opcao == 2:
        for saque in extrato:
            print(saque)
            print(30 * "=")
        print(f"Lançamentos: {len(extrato)}")
        print(f"Valor disponível: R${saldo:.2f}")
        primeiro_acesso = 1
        input("pressione ENTER para continuar")

    elif opcao == 3:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
