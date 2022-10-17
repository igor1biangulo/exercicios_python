"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False

temperatura = []

for i in range(0,2):

    dado = input(f"digite temperatura {i} ")
    while True:
        if is_float(dado):
            temperatura.append(dado)
            break

        else:
            print("digite somente numeros inteiros ")

valor = sum(temperatura)

print(valor)






 