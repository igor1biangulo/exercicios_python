"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
def somaImposto(taxaImposto,valordoproduto):
    calculo1 = (taxaImposto*valordoproduto)/100
    return calculo1 + valordoproduto

imporsto = float(input("digite a porcentagem,sem o simbolo: "))
produto =  float(input("digite o valor do produto"))
result = somaImposto(imporsto,produto)
print(f"seu produto com valor somado aos importos e {result}")




    