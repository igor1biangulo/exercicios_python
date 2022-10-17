from random import shuffle

def aleatorio(palavra):
    lista_da_palavra = list(palavra)
    shuffle(lista_da_palavra)
    return lista_da_palavra

pavavra_a_ser_embaralhada = input("digite uma palavra: ")
pavavra_a_ser_embaralhada = pavavra_a_ser_embaralhada.upper()
result = aleatorio(pavavra_a_ser_embaralhada)
print(*result)
"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

    
