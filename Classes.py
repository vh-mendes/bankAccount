class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self._saldo += valor_deposito
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido, tente novamente por favor.")

    def sacar(self, valor_saque):
        if valor_saque > self._saldo:
            print("Você não tem saldo suficiente.") 
        else: 
            self._saldo -= valor_saque 
            print("Saque realizado com sucesso!")

    def get_saldo(self):
        return self._saldo
    
    def get_titular(self):
        return self._titular
        
class ContaCorrente(ContaBancaria):
       def __init__(self, titular, saldo, limite=500):
            super().__init__(titular, saldo)
            self.limite = limite

       def sacar(self, valor):
            if valor > (self._saldo + self.limite):
                print("Você não tem saldo suficiente.") 
            else:
                self._saldo -= valor 
                print(f'Saque de R${valor:.2} realizado. Saldo atual: R${self._saldo}.')

class OperacoesBancarias:
    def transferencia(self, conta_origem, conta_destino, valor):
        if conta_origem._saldo >= valor:
            conta_origem._saldo -= valor
            conta_destino._saldo += valor
            print(f'Transferencia R${valor:.2f} realizada com sucesso')
        else:
            print("Você não tem saldo para realizar a transferência.")
  
class ContaInvestimento:
    def investir(self, valor):
        print(f'Investido R${valor:.2f} no fundo de investimento.')

class ContaPremium(ContaBancaria, OperacoesBancarias, ContaInvestimento):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
