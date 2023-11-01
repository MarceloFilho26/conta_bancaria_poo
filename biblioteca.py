class ContaBancaria:
    def __init__(self, numero_conta, nome_cliente, tipo_conta):
        self.saldo_conta = 0
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.cheque_especial = 0
        self.status_conta = False
        self.ativar_conta = False
        self.desativar_conta = False


    def verificarSaldo(self):
        if self.status_conta == True:
            print(f"Saldo da conta é de: R${self.saldo_conta} e cheque especial é de: R${self.cheque_especial}.")
        else:
            print("Conta desativada, impossível verificar o saldo.")

    def sacar(self, saque):
        if self.status_conta == True:
            if self.saldo_conta + self.cheque_especial < saque:
                print("Valor maior que o disponível em conta.")
            elif saque == 0:
                print("Valor inválido para sacar.")
            else:
                if saque > self.saldo_conta:
                    valor_saque = saque - self.saldo_conta
                    self.saldo_conta = 0
                    self.saldo_conta -= self.cheque_especial
                    self.cheque_especial -= valor_saque
                else:
                    self.saldo_conta -= saque
                print(f"Saque de R${saque} realizado com sucesso.")
        else:
            print("Impossível realizar saques em contas desativadas.")

    def depositar(self, deposito):
        if self.status_conta == True:
            if self.saldo_conta < 0:
                self.saldo_conta += deposito
                self.cheque_especial += (deposito - self.saldo_conta)
                print(f"Deposito realizado com sucesso. Saldo atual de R${self.saldo_conta} e cheque especial de R${self.cheque_especial}")
            else:
                self.saldo_conta += deposito
                print(f"Deposito realizado com sucesso. Saldo atual de R${self.saldo_conta}")
        else:
            print("Conta desativada, impossível realizar deposítos.")

    def ativarConta(self):
        if self.ativar_conta == False:
            self.ativar_conta = True
            self.status_conta = True
            print("Conta ativada com sucesso!")
        else:
            print("A conta já está ativada.")

    def desativarConta(self):
        if self.saldo_conta > 0:
            print("Impossível desativar conta com saldo positivo.")
        elif self.status_conta == True:
                self.ativar_conta = False
                self.status_conta = False
                self.desativar_conta = True
                print("Conta desativada com sucesso!")
        else:
            print("A conta já está desativada.")

    def ativarLimite(self, limite):
        if self.status_conta == True:
            self.cheque_especial += limite
            print(f"Limite ativado, seu novo limite é de R${limite}.")
        else:
            print("Impossível ativar limite em conta desativada.")
