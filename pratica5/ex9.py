"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""
#receber o numero
def reverso(num1):
    lista=[]
    num1 = str(num1)
    lista.append(num1)
    return num1[::-1]

num = int(input("digite um numero: "))
result = reverso(num)
print(result)

