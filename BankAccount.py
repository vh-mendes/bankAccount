from Classes import * ##Ou seja, importar tudo

conta_vitor = ContaPremium("Vítor Hugo", 2900)
conta_otario = ContaPremium ("Otário Castro", 1)


conta_vitor.transferencia(conta_vitor, conta_otario, 500)
conta_otario.investir(501)
print(f'Saldo Vitor: R${conta_vitor.get_saldo()}')
print(f'Saldo Otario: R${conta_otario.get_saldo()}')
conta_vitor.sacar(1000)
print(f'Vitor: R${conta_vitor.get_saldo()}')
conta_vitor.sacar(1200)
print(f'Saldo Vitor: R${conta_vitor.get_saldo()}')
