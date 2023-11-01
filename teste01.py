from biblioteca import *
p1 = ContaBancaria(10001, "Marcelo", "Corrente")
p1.ativarConta()
p1.ativarLimite(1000)
p1.depositar(2000)
p1.sacar(3000)
p1.verificarSaldo()
p1.depositar(3000)
p1.verificarSaldo()
