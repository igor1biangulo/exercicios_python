"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
print("vaja seu novo salario e quantos porcento vc ganhou")
salary = float(input("quanto vc recebe atualmente: "))
if salary <= 280.00:
    x = 20 * salary
    y = x / 100
    z = salary + y
    print(f"seu salario era de {salary}\no percentual de aumento foi de 20%\no valor do aumento foi de {y}\ne seu novo salario e de {z}")
elif salary > 280.00 and salary < 700:
  x = 15 * salary
  y = x / 100
  z = salary + y
  print(f"seu salario era de {salary}\no percentual de aumento foi de 15%\no valor do aumento foi de {y}\ne seu novo salario e de {z}")
elif salary > 700 and salary < 1500:
    x = 10 * salary
    y = x / 100
    z = salary + y
    print(f"seu salario era de {salary}\no percentual de aumento foi de 10%\no valor do aumento foi de {y}\ne seu novo salario e de {z}")
elif salary > 1500:
    x = 5 * salary
    y = x / 100
    z = salary + y
    print(f"seu salario era de {salary}\no percentual de aumento foi de 5%\no valor do aumento foi de {y}\ne seu novo salario e de {z}")



    