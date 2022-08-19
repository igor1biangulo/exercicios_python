"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
print("4 notas e a media ")
vetor = []
entrada = input("[s][n]")
while entrada == "s":
    for i in range(0,4):
        num = float(input("nota " + str(i + 1) + ": "))
        vetor.append(num)
        soma = sum(vetor)
        print(soma)
    break
print("-------------------------------------")
media = soma/4
print(f"suas nota são {vetor}\nelas somada dão [{soma}]\nsua media e [{media}]")

