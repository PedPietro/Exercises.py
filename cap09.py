'''
9.1. Crie tabelas semelhantes às dos exemplos para relacionar os divisores de 14, 24, 37
9.2. Codifique um programa que leia um número natural e informe quais são os seus divisores.
9.3. Codifique um programa que leia um número natural e informe se ele é ou não primo.
9.4. Codifique um programa que exiba na tela todos os números primos entre 1 e um valor final
informado pelo usuário. Ao final da exibição da relação de números primos, deve-se exibir
a somatória, a média aritmética e a média harmônica dos valores primos encontrados e
exibidos nesse intervalo, por meio do uso da classe Somatoria enquanto se buscam os
primos
'''

def ex9_4():
    numero = float(input("Digite o número desejado: "))
    i = 0
    for i  in range(1, numero, 1):
        if numero % i == 0:
            divisores +=1
            i += 1
