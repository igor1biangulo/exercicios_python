"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor1 =[]
vetor2=[]
vetor3 =[]
for i in range(0,10):
    vetor1.append(input("digito "+str(i+1)+" do vetor 1: "))
    
for i in range(0,10):
    vetor2.append(input("digito "+str(i+1)+" do vetor 2: "))

for i in range(0,20):
    for x in range(1):
        vetor3.append(vetor1[x])
    for z in range(1):
        vetor3.append(vetor2[z])
   


print(f"vetor1: {vetor1}\nvetor 2: {vetor2}\njuntos fazem o vetor 3: {vetor3}")

