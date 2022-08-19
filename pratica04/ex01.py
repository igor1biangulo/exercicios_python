"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
print("ler e mostra 5 numero em um vetor")
vetor = []
for i in range(4):
    num1 = input("digite o numero " + str(i + 1) + ": ")
    if num1.isnumeric():
        num1 = int(num1)
        vetor.append(num1)
    else:
        print("esse digito n vai pro vetor pq n e um numero inteiro") 
        
print(vetor)

