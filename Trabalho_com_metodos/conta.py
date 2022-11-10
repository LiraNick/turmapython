class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"{self.titular} - {self.numero} - {self.saldo} - {self.limite}")

    def depositar(self, valor): 
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)

        
