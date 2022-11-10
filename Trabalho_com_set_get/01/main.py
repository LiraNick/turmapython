from conta import Conta

print("*"*30, "Criação de Conta", "*"*30)

conta = Conta(input("Digite Seu Nome:> "), 
int(input("Digite o N° da Conta:> ")),
float(input("Digite Seu Saldo:> ")),
float(input("Digite o Limite Sem Mentir:> ")))

print("*"*30)
print("o Nome do titular é {} o numero da conta é {} e o saldo é {}.".format(conta.get_titular(), conta.get_numero(), conta.get_saldo()))
print("*"*30)