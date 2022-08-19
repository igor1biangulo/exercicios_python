"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
print("leis 10 numeros reais e o mostreos")
vetor = []
entrada = input("[s][n]")
while entrada == "s":
    for i in range(0,10):
        num = float(input("numero" + str( i + 1) + ": "))
        vetor.append(num)       
    break
print(vetor)

