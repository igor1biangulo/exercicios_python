"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor1=[]
vetor2=[]
vetor3=[]
vetor4=[]
for i in range(0,10):
    vetor1.append(input("digito "+str(i+1)+" do vetor 1: "))
for i in range(0,10):
     vetor2.append(input("digito "+str(i+1)+" do vetor 2: "))
for i in range(0,10):
     vetor3.append(input("digito "+str(i+1)+" do vetor 2: "))
for i in range(0,30):
     for x in range(1):
          vetor4.extend(vetor1[x])
     for y in range(1):
          vetor4.extend(vetor2[y])
     for z in range(1):
          vetor4.extend(vetor3[z])


print(f"vetor1: {vetor1}\nvetor 2: {vetor2}\nvetor 3: {vetor3}\njuntos fazem o vetor 3: {vetor4}")