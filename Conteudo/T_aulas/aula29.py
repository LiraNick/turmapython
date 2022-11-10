class Conta:

    def __init__(self, numero, titular, saldo, cpf, limite):
        print(f"Imprimindo variavel de referencia{self}")


        self.numero = numero
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo 
        self.limite = limite
