'''Problema: Um círculo de raio 2 é colocado dentro de um retângulo de lados 5 e 7
Faça um programa que informe o tamanho da área do retângulo que não está sendo ocupada pelo círculo
Obs: Decidi fazer um programa mais geral que solicitasse o usuário os valores de entrada, mas restringi que fosse um círculo interno ao retângulo!'''

import math

def calcular_area_circulo(raio):
    return math.pi*(raio**2)

def calcular_area_retangulo(comprimento, altura):
    return comprimento*altura

def ler_valor_positivo(num):
    while True:
        try:
            valor = float(input(num))
            if valor > 0:
                return valor
            else:
                print("Por favor, escolha um valor positivo")
        except ValueError:
            print("Entrada inválida! Digite um valor válido")

while True:
    r = ler_valor_positivo("Digite o valor para o raio do círculo: ")
    a = ler_valor_positivo("Digite o valor para o comprimento do retângulo: ")
    b = ler_valor_positivo("Digite o valor para a altura do retângulo: ")

    if (r>(a/2) or r>(b/2)):
        print("Digite valores válidos para o cálculo")
    else:
        break

diferenca = calcular_area_retangulo(a,b) - calcular_area_circulo(r)
print(f"A diferença entre as áreas é de {diferenca:.2f}")
