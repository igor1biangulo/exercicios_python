"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

while True:
    numero1 = input("digite um numero: ")
    numero2 = input("digite outro numero: ")
    if numero1.isnumeric() and numero2.isnumeric():
        numero1,numero2 = int(numero1), int(numero2)
        break
    else:
        print("digita certo, tem que ser numeros inteiros")

if numero1 > numero2:
    lado = numero2
    while lado+1 < numero1:
        numero1 -=1
        print(numero1)

elif numero2 > numero1:
    for i in range(numero1+1,numero2):
        print(i)

