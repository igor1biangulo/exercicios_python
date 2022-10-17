"""
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n"""

def funcao(n=input("digite um numero: ")):
    lista = [1]
    conta = 1
    if n.isnumeric():
        n=int(n)
        for i in range(n):
            print(*lista)
            conta += 1
            lista.append(conta)
    else:
        print("digite somente numeros inteiros")

funcao()













