class Animal():
    espécie = ""
    cor = ""
    raça = ""
    valor = 0
    def __str__(self):
        return f" {self.espécie} - {self.cor} - {self.raça} - {self.valor}"