telaInicial = open('tela01.txt')
content = telaInicial.readlines()

for i in range(14):
    print(content[i].strip("\n"))
    