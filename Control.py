from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.num1  = 0
        self.num2  = 0
        self.modelo = Model() #Conectando com a classe model

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def coletar(self):
        print("Informe um número: ")
        self.setNum1(float(input()))

        print("Informe outro número: ")
        self.setNum2(float(input()))

    def menu(self):
        print("\nEscolha uma das opções abaixo: " +
              "\n0. Sair"                         +
              "\n1. Somar"                        +
              "\n2. Subtrair"                     +
              "\n3. Dividir"                      +
              "\n4. Multiplicar"                  +
              "\n5. Potência"                     +
              "\n6. Raiz"                         +
              "\n7. Tabuada")
        self.setOpcao(int(input())) #Coletando a escolha do usuário

    def operacao(self):
        while(self.getOpcao != 0):
            self.menu() #Mostrar a lista de dados na tela
            if self.getOpcao() == 0:
                print("Obrigado!")
                break
            elif self.getOpcao() == 1:
                self.coletar()
                print("O resultado da soma dos dois números é: {}".format(self.modelo.soma(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 2:
                self.coletar()
                print("O resultado da subtração dos dois números é: {}".format(self.modelo.subtracao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 3:
                self.coletar()
                resultado = self.modelo.divisao(self.getNum1(), self.getNum2())
                if resultado == -1:
                    print("Impossível dividir por zero!")
                else:
                    print("O resultado da divisao dos dois números é: {}".format(resultado))
            elif self.getOpcao() == 4:
                self.coletar()
                print("O resultado da multiplicação dos dois números é: {}".format(self.modelo.multiplicacao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 5:
                self.coletar()
                print("O resultado é {}".format(self.modelo.potencia(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 6:
                print("Informe um número para calcular a raiz: ")
                resultado = self.modelo.raiz(float(input()))
                if resultado == -1:
                    print("Impossível calcular a raiz!")
                else:
                    print("O resultado é {}".format(resultado))
            elif self.getOpcao() == 7:
                print("Informe um número: ")
                print(self.modelo.tabuada(float(input())))
            else:
                print("Opção invalida!")



