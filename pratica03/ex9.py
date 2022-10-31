"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

for i in range(0,51,2):
    if i == 1:
        print("os numeros pares entre 1 e 50 são ")
    if i > 1:
        print(f"{i}", end = " ")