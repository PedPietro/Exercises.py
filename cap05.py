def seletor_de_opcoes():
    escolha = "0"
    while escolha != "":
        print("Operações Disponíveis")
        print("=======================\n")
        print("5-2")
        print("5-3")

        escolha = input("Que operação deseja fazer: ")
        match escolha: 
            case "1": ex5_2()
            case "2": ex5_3()


def ex5_2():
    total = 2
    for i in range(5) :
        total = total * 2
    print(f"O total é: {total}")

#64

# 5.3. Faça um programa em Python que imprima todos os múltiplos de N, entre um valor inicial e
#um valor final.
#Para saber se um número é múltiplo de N, você pode fazer if (numero % n == 0).
#Os valores inteiros N, valor inicial e valor final devem ser lidos pelo teclado.
def ex5_3():
    valor_inicial = int(input("Digite o valor inicial: "))
    valor_final = int(input("Digite o valor final: "))
    N = int(input("Digite o valor de N: "))
    if (valor_inicial % N == 0):
        if(valor_final % N == 0):
            total = 1
            for x in range(valor_inicial,valor_final):
                total = total * N
                print(f"{x}")
        else:
            print("valor final inválido!")        
    else:
        print("valor inicial inválido!")