from Classes import ContaBancaria

conta1 = ContaBancaria("Vitão Bonitão", 1002)

print(conta1.get_titular(), "seu saldo é:", conta1.get_saldo())

valorDeposito = int(input("Digite o valor do depósito: "))
conta1.depositar(valorDeposito)

print(conta1.get_titular(), " seu saldo atualizado é:", conta1.get_saldo())

valorSaque = int(input("Digite o valor que você deseja sacar: "))
conta1.sacar(valorSaque)

print(conta1.get_titular(), ",seu saldo atualizado é:", conta1.get_saldo())


