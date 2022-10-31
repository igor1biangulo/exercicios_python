"""
Faça um programa que leia 5 números e informe o maior número.
"""
controle =0
for i in range(1,6):
    numero = input(f"{i}-numero: ")
    if numero.isnumeric():
        numero = int(numero)
        if controle < numero:
            controle = numero

print(f"meior numero digitado foi {controle}")