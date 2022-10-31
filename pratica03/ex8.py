"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0
for i in range(1,6):
    numero = input(f"{i}-numero: ")
    if numero.isnumeric():
        numero = int(numero)
        soma = numero + soma
    else:
        print("falow vc digitou errado")
        


print(f"media entre os numero e {soma/5}")