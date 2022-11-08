#EXERCICIO-01 crie um documento instanciando uma classe chamada conta, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória, acessando diretamente o objeto de conta insira dados internos na função através da variável referência padrão, e insira atributos recebendo valores internos número, titular, saldo, limite.
#segundo encapsulamento methodo
class Conta:
    #terceiro encapsulamento
    def __init__(self, numero, titular, saldo, cpf, limite):
        print(f"Imprimindo variavel de referencia{self}")


        self.numero = numero
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo 
        self.limite = limite
    
    def extrato(self):
        print("o numero da conta {} do {} tem o valor".format(self.numero, self.titular, self.cpf, self.saldo, self.limite))

    def depositar(self, valor):
        self.saldo += valor
        return valor