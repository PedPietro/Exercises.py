def menu():
    opcao = ""
    while True:
        print("\nSelecione o exercício para executar:")
        print("1 - Exercício 2-1")
        print("2 - Exercício 2-2")
        print("3 - Exercício 2-3")
        print("4 - Exercício 2-4")
        print("5 - Exercício 2-5")
        print("6 - Exercício 2-6")
        print("7 - Exercício 2-7")
        print("8 - Exercício 2-8")
        print("9 - Exercício 2-9")
        print("0 - Sair")
        
        opcao = input("Digite sua escolha: ")
        match opcao:
            case "1":ex2_1()
            case "2":ex2_2()
            case "3":ex2_3()
            case "4":ex2_4()
            case "5":  ex2_5()
            case "6":   ex2_6()
            case "7":ex2_7()
            case "8":ex2_8()
            case "9":ex2_9()
            case "0":
                print("Fim do programa")
                break 
        if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            print("Opção inválida")
        
# Função do arquivo 2-1.py
def ex2_1():
    a = float(input("Digite o valor do a: "))
    y = a + 151 
    c = 7
    b = c * (144 + y) 
    x = y + (a * b / c) 
    print(f"O valor de x é: {x}")

# Função do arquivo 2-2.py
def ex2_2():
    nota1 = float(input("Digite a sua nota no 1° Bimestre: "))
    nota2 = float(input("Digite a sua nota no 2° Bimestre: "))
    nota3 = float(input("Digite a sua nota no 3° Bimestre: "))
    nota4 = float(input("Digite a sua nota no 4° Bimestre: "))
    notaFinal = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Sua média aritmética é: {notaFinal}")

# Função do arquivo 2-3.py
def ex2_3():
    m = float(input("Digite o valor em m: "))
    cm = m * 100
    print(f"O valor {m}m em cm é: {cm}")

# Função do arquivo 2-4.py
def ex2_4():
    raio = float(input("Digite o tamanho do raio: "))
    pi = 3.14
    circulo = (raio * raio) * pi
    print(f"O tamanho do círculo é: {circulo}")

def ex2_5(): 
    ganhoHora = float(input("Digite quando você ganha por hora: "))
    qtasHorasMes = float(input("Digite horas você trabalha por Mês: "))
    salario = ganhoHora  * qtasHorasMes
    print(f"Você ganha {salario}!")
    
def ex2_6():
    inteiro1 = int(input("Digite o valor do 1°Inteiro: "))
    inteiro2 = int(input("Digite o valor do 2°Inteiro: "))
    real =  float(input("Digite o valor do Real: "))
    primeiro = (2*inteiro1) * (inteiro2/2)
    segundo = (3 * inteiro1) + real
    terceiro = real ** 3
    print(f"{primeiro}")
    print(f"{segundo}")
    print(f"{terceiro}")

def ex2_7():
    h = float(input("Digite sua altura: "))
    pesoIdeal = (62.1 * h) - 44.7
    print(f"O seu Peso ideal é: {pesoIdeal}")

def ex2_8():
    primeiro = int(input("Digite o 1° valor: "))
    segundo = int(input("Digite o 2° valor: "))
    soma = primeiro + segundo
    subtracao = primeiro - segundo
    multiplicacao = primeiro * segundo
    divisao = primeiro /segundo
    divisaoInt = primeiro // segundo
    elevado = primeiro ** segundo
    restoDivisao = primeiro % segundo 
    
    print(f"O resultado é: {soma}")
    print(f"O resultado é: {subtracao}")
    print(f"O resultado é: {multiplicacao}")
    print(f"O resultado é: {divisao}")
    print(f"O resultado é: {divisaoInt}")
    print(f"O resultado é: {elevado}")
    print(f"O resultado é: {restoDivisao}")

def ex2_9():
    areaPintada = float(input("Digite o tamanho da area a ser pintada em m²: "))
    tinta = areaPintada // 3
    y = 0
    if tinta % 3 > 0:
        y = 1
    quantidadeLatas = (tinta + y) // 18
    valorGasto = 80 * quantidadeLatas
    z = 0
    if quantidadeLatas % 18 > 0:
        z = 1
    print(f"A quantidade latas a serem comprada vai ser: {quantidadeLatas + y}")
    print(f"O valor a ser gasto vai ser: {valorGasto + (80 * z)} ")
    
if __name__ == "__main__":
    menu()