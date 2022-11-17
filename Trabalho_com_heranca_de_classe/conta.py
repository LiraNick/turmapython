class Conta:

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print("Passando Pelo Constrtutor da Classe Mae")

    def __str__(self):
        return f"O numero da conta é:> {self.numero}\nO tipo da conta é:> {self.tipo}"

