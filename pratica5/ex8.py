"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

"""
#
def recebe(num1):
    return len(num1)


num1 = input("digite um numero inteiro: ")
if num1.isnumeric():
    result = recebe(num1)
    print(result)
else:
    print("somente numeros inteiro,são permitidos")

