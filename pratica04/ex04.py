"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
import time
def linha():
    print("----------------------------------------")
print("consoante ou vogal")
vogal = "a e i o u"
x = "a s d f g r a s d t"
t = x.split(" ")
digiti = []
vogalvetor = vogal.split(" ")
print(vogalvetor)

comeco = input("[s][n]")
contador = 0

while comeco=="s": 
    digiti.clear()
    if contador == 10:
        break
    for i in range(0,10):
        digito = input("digito "+str(i + 1)+": ")
        
        if digito.isnumeric():
            print("digite somente letras")
            break
        else: 
                   
            digiti.append(digito)
    contador += 1
    
    comeco = input("deseja tentar de novo? [s]sim [n]não: ")

print(digiti)
vogal_final = []
consoante_final = []
for i in range(0,10):
    
    if digiti[i] in "aeiou":
        print(f"[{digiti[i]}] e uma vogal")
        vogal_final.append(digiti[i])

    else:
        print(f"[{digiti[i]}] e uma consoante")
        consoante_final.append(digiti[i])

print(f"vogal: {vogal_final}\nconsoantes: {consoante_final}")

        
        

    

    

    
    
