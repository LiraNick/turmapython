# EXERCICIO-02 crie um documento instanciando uma classe chamada conta, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória,  defina os atributos diretamente na função construtor número, titular, saldo, limite, crie um segundo documento main com variável conta 1, conta 2, conta 3 , insira valores diferentes para cada objeto, imprima no terminal o espaço  alocado de memória do objeto principal , e de cada variável de referência para o objeto!
from Exercicio05 import Conta

conta1 = Conta(123, "nicolau", 60606060, 500, 1200.0)
conta2 = Conta(321, "lirinha", 24242424, 800, 1500.0)
conta3 = Conta(654, "nickzera", 69696969, 300, 3200.0)

print("="*30)
print(conta1)

print("="*30)
print(conta2)

print("="*30)
print(conta3)

conta1.extrato()
