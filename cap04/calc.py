import os

class Calculadora:
    def __init__(self):
        self.priNumero = 0.0
        self.segNumero = 0.0
        self.result = 0.0
        
    def ObterNumeros(self):
        self.priNumero = float(input("Digite o 1º valor:"))
        self.segNumero = float(input("Digite o 2º valor:"))

    def Somar(self):
        self.result = self.priNumero + self.segNumero
        
    def Subtrair(self):
        self.result = self.priNumero - self.segNumero

    def Dividir(self):
        self.result = self.priNumero / self.segNumero

    def Multiplicar(self):
        self.result = self.priNumero * self.segNumero

    def ExibirResultado(self, operador):
        print(f"{self.priNumero} {operador} {self.segNumero} vale {self.result}.")
        
    def LimparVisor(self):
        os.system('cls') or None	# limpa a tela no S.O. Windows
        self.result = 0.0
  
    def Ligar(self):
        self.LimparVisor()		# chama a execução do método LimparVisor()
        self.priNumero = 0.0
        self.segNumero =0.0
  
    def Desligar(self):
        self.LimparVisor()
        print("Saindo da memória!")  