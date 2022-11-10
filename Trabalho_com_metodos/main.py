from conta import Conta

print("*"*30, "Criação de Conta", "*"*30)

conta = Conta(input("Digita o nome ai:> "), 
int(input("Digita o numero da conta ai:> ")),
float(input("Digita seu saldo inicial ai:> ")),
float(input("Digite o limite sem mentir:> ")))

print("*"*30, "Extrato Inicial", "*"*30)
conta.extrato()

print("*"*30,)
print(conta.depositar(float(input("Digite o valor do deposito:> "))))

print("*"*30, "Extrato Deposito", "*"*30)
conta.extrato()

print("*"*30,"\n")

print(conta.sacar(float(input("Digite o valor que ce quer roubar:> "))))
print("*"*30, "Extrato Saque", "*"*30)
conta.extrato()

print("*"*30, "Criação de Conta2.0", "*"*30)

conta2 = Conta(input("Digita o nome ai:> "), 
int(input("Digita o numero da conta ai:> ")),
float(input("Digita seu saldo inicial ai:> ")),
float(input("Digite o limite sem mentir:> ")))

print("*"*30, "Extrato Inicial", "*"*30)
conta2.extrato()

print("*"*30,)
print(conta2.depositar(float(input("Digite o valor do deposito:> "))))

print("*"*30, "Extrato Deposito", "*"*30)
conta2.extrato()

print("*"*30,"\n")

print(conta2.sacar(float(input("Digite o valor que ce quer roubar:> "))))
print("*"*30, "Extrato Saque", "*"*30)
conta2.extrato()
