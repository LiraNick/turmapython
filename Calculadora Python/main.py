from tkinter import Menu
from Conteudo.aula25 import soma
import Controller

poli = ('-'*15)
print(f"{poli} "calculadora" {poli} \n1.Soma. \n2.Subtracao. \n3.Multiplicacao. \n4.Divisao. \n0.Sair")
var = int(input("digite a operação selecionada:"))
menu= 1
while (menu!=0):
    menu = int(input("digite a operação selecionada:"))
    match var:
        case 1:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            Controller.soma(n1,n2)
        case 2:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            Controller.subtracao(n1,n2)
        case 3:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            Controller.multiplicacao(n1,n2)
        case 4:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            Controller.divisao(n1,n2)