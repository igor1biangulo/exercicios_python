"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
print("mostre o menos entre os tres numero")
num1 = int(input("digite numero 1: "))
num2 = int(input("digite numero 2: "))
num3 = int(input("digite numero 3: "))
menor = num1
if num1 < menor:
    menor = num2
if num2 < menor:
    menor = num3
print(f"o menor numero entre os tres e {menor}")