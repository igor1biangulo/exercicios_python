"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""
def posi_ou_nega(num1):
    if num1 < 0:
        return "n"
    if num1 >= 0:
        return "p"

respo = posi_ou_nega(9)
print(respo)
     
