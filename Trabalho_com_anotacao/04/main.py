from pessoa import Pessoa

print("*"*30, "Criando RG", "*"*30)

pessoa = Pessoa(input("Digite Seu Nome:> "), 
int(input("Digite Seu Cpf:> ")),
int(input("Digite Sua Idade:> ")),
float(input("Digite Sua Altura:> ")))

print("*"*30)
print("o Nome é {} o cpf é {} a idade é {} e a sua altura é {}.".format(pessoa.get_nome(), pessoa.get_cpf(), pessoa.get_idade(), pessoa.get_altura()))
print("*"*30) 