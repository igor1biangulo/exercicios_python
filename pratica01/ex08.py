"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
print("calculando seu salario")
sal = float(input("coloque quando vc ganha por hora trabalhada"))
hr = float(input("quantas hrs vc trabalha por dia "))
dias = int(int("e quantos dias na semana: "))
print(f"seu salario do mes vai ser {sal * hr * dias} ")