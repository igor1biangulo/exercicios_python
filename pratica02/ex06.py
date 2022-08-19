"""
Faça um Programa que leia três números e mostre o maior deles.
"""
print("mostre entre tres numero qual e o maior")
num1 = float(input("digite o numero 1: "))
num2 = float(input("digite o numero 2: "))
num3 = float(input("digite o numero 3: "))
maior = num1
if num1 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f"o maior numero entre os tres e {maior}")