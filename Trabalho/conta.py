class Conta:
    __titular = ""
    __numero = 0
    __saldo = 0

    @property #getter
    def titular(self):
        return self.__titular
    @titular.setter #setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular}; {self.numero}; {self.saldo}"