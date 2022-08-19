"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
print("preços menor")
num1 = int(input("digite o primeiro preço "))
num2 = int(input("digite o segundo preço "))
num3 = int(input("digite o terceiro preço "))
menor = num1
if num1 < menor:
    menor = num2
if num2 < menor:
    menor = num3
print(f"o menor preço e   {menor}")