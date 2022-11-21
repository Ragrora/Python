MENU = """

[1] Saque
[2] Desposito
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "1":

        saque = float(input("Quanto deseja sacar: "))
        

        if saque > 0:

            if saque < limite:

                if numero_saques < LIMITE_SAQUES:

                    if saque < saldo:
                        print("Saque realizado com sucesso!")

                        numero_saques += 1
                        saldo -= saque
                        extrato += f"Saque: - R$ {saque:.2f}\n"

                    else:
                        print("Operação recusada: Saldo insuficiente.")
                
                else:
                    print("Operação recusada: Limite de saques diários atingido.")

            else:
                print("Operação recusada: Limite indisponível.")
        else:
            print("Insira um valor válido.")

    if opcao == "2":

        deposito = float(input("Insira a quantidade de sejesa depositar: "))

        if deposito > 0:

            saldo += deposito
            extrato += f"Depósito: + R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Insira um valor válido.")        

    if opcao == "3":
        
        print("Não forma realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    if opcao == "4":
        break