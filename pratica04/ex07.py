"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
from math import prod
vetor = []
for i in range(0,5):
    num = input("numero " + str(i + 1) + ": ")
    if num.isnumeric():
        num = int(num)
        vetor.append(num)
    else:
        print("numero n e valido reinicie o programa")
        break
soma = sum(vetor)
multi = prod(vetor)
print(f"a soma de todos os numero do vetor e {soma}\n a multiplicaçao de todos os numero do vetor e {multi}\ne todos os numeros do vetor e {vetor}")
