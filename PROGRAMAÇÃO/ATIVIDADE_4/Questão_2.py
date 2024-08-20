class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo  
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        
    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += int(valor)
        print(f"Valor de {valor} reais foi depositado na conta {self.numero_conta}.")
    
    def sacar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        if int(valor)  <= self.saldo and int(valor)  >= 1:
            self.saldo -= int(valor) 
            print(f"Saldo sacado com sucesso: {valor}")

        elif int(valor)  == 0:
            print("Valor de saque é 0.")

        else:
            print("Valor inválido!")
    
    def transferir(self):  
        va = float(input("Digite o valor a transferir: "))
        marcus.saldo -= va
        lucas.saldo += va
        print(f"Saldo: {lucas.saldo}")


    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


marcus = ContaBancaria("marcus", 10000.00, "8787", "CP")
lucas = ContaBancaria("lucas", 87.12, "8787", "CC")


form = "\n----- Caixa Econômica! -----\n\n1 - DEPOSITAR\n2 - SACAR\n3 - TRANSFERIR\n4 - VERIFICAR SALDO\n\n\nOpção:"


deci = "a"
while deci == "a":
    recebe = input(form)
    if recebe == '1':
        lucas.depositar()

    elif recebe == "2":
        lucas.sacar()

    elif recebe == "3":
        lucas.transferir()

    elif recebe == "4":
        lucas.verificar_saldo()

    else:
        print("Opção inválida.")

    conti = input("Deseja continuar? (S/N) ").strip().upper()
    if conti == "S" or conti == "SIM":
        continue
    else:
        deci = "b"
