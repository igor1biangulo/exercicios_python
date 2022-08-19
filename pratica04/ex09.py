"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
print("some e eleve ao quadrado")
vetora = []
soma = 0
for x in range(0,10):
    vetora.append(int(input("numero " + str(x + 1) + ": ")))
    soma = soma + (vetora[len(vetora)-1]**2)
print(soma)

