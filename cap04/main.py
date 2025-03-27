import cap04.calc as calc
import os


def seletor_de_opcoes():
    print("Operações Disponíveis")
    print("=======================\n")
    print("0 - Terminar programa")
    print("9 - Digitar os dois números")
    print("+ : Adicionar dois números")
    print("- : Subtrair dois números")
    print("x : Multiplicar dois números")
    print("/ : Dividir dois números")
    escolha = input("Que operação deseja fazer: ")
    return escolha

def realizar(operacao, umaCalc):
    if operacao == "9":
        umaCalc.ObterNumeros()
    elif operacao in "x-+/": 
            if operacao =="+":
                umaCalc.Somar()
                umaCalc.ExibirResultado('+')
            elif operacao =="-":
                umaCalc.Subtrair()
                umaCalc.ExibirResultado('-')
            elif operacao =="/":
                umaCalc.Dividir()
                umaCalc.ExibirResultado('÷')
            else:
                umaCalc.Multiplicar()
                umaCalc.ExibirResultado(operacao)
    else:
        print("Operação inválida!")
        
def executar():
    umaCalc = calc.Calculadora()
    umaCalc.Ligar()
    
    operacao = "#"
    while operacao != "0":
        operacao = seletor_de_opcoes()
        if operacao != "0":
            realizar(operacao, umaCalc)

    umaCalc.Desligar()

# Bloco Principal

if __name__ == "__main__":
    os.system('cls') or None
    executar()
    espera = input("Digite [Enter] para terminar este programa")
    print("Obrigado")
