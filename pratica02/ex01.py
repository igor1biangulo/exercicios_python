"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
print("ver qual e o numero maior")
num = input("digite um numero: ")
num2 = input("digite outro numero: ")
if num.isnumeric() and num2.isnumeric():
    num = int(num)
    num2 = int(num2)
    if num > num2:
        print(f"{num} e maior que {num2} ")
    elif num2 > num:
        print(f"{num2} e maior que {num}")
