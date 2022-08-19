"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida
"""
def linha():
    print("---------------------------------")

print("ideda,altura... agora inverti")
idade = []
altura = []
for1 = 5
for i in range(0,5):
    idade.append(int(input("idade da pessoa "+ str(i + 1) +": ")))
    altura.append(int(input("altura da pessoa "+ str(i + 1) +": ")))

for x in range(0, 5):
    linha()
    print(f"pesoa {for1}\nidade: {idade[len(idade)-1-x]}\naltura: {altura[len(altura)-1-x]}")
    for1 -= 1 
    

    


