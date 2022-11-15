from conta import Conta
class PessoaJuridica(Conta):
    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__("3050", 500, "Pessoa Juridica")
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial
        print("Passando Pelo Construtor da Classe Pessoa Juridica")
    __segundo_titular = ""
    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__}\nTitular:> {self.titular}\nCnpj:> {self.cnpj}\nSaldo inicial:> {self.saldo_inicial}\nSegundo titular:> {self.segundo_titular}"