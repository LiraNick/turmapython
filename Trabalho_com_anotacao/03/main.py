from conta import Conta

print("*"*30, "Banco", "*"*30)

conta = Conta(input("Digite Seu Nome:> "),
int(input("Digite Seu Numero:> ")),
int(input("Digite Seu Saldo:> ")),
int(input("Digite Seu Limite:> ")))

print("*"*30)
print(f"o titular da conta é o  {conta.titular} e o numero da conta {conta.numero}, seu saldo é {conta.saldo}.")
print("*"*30)  