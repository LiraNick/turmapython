from conta import Conta
class PessoaFisica(Conta):
    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__("2050", 500, "Pessoa Fisica")
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial
        print("Passando Pelo Construtor da Classe Pessoa Fisica")
    __segundo_titular = ""
    @property #getter
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter #setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__}\nTitular:> {self.titular}\nCpf:> {self.cpf}\nSaldo inicial:> {self.saldo_inicial}\nSegundo titular:> {self.segundo_titular}"