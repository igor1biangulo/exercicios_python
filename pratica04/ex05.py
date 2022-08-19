"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
par = []
impar = []
for i in range(0,20):
    num = input("numero " + str(i + 1) + ": ")
    if num.isnumeric():
        num = int(num)
        if num  %2 ==0:
            par.append(num)

        else:
            impar.append(num)
    else:
        print("seu numero n e valido reinicie o programa")
        break
print(f"numeros: {par}\nnumeros: {impar}")
print("fim")
