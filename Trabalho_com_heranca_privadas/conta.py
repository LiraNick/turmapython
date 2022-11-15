class Conta:

    def __init__(self, numero, agencia, tipo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        print("Passando Pelo Constrtutor da Classe Mae")

    def __str__(self):
        return f"O numero da conta é:> {self.numero}\nO tipo da conta é:> {self.tipo}\nA agencia da conta é:> {self.agencia}"
