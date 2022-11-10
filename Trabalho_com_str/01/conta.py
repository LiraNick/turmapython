class Conta:
    titular = ""
    numero = 0
    saldo = 0
    limite = 0
    def __str__(self):
        return f"{self.titular} - {self.numero} - {self.saldo} - {self.limite}"