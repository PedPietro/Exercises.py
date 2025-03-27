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
def ex2__4():
    raio = float(input("Digite o tamanho do raio: "))
    pi = 3.14
    circulo = (raio * raio) * pi
    print(f"O tamanho do círculo é: {circulo}")

# Chamadas das funções
ex2_1()
ex2_2()
ex2_3()
ex2__4()