"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
""" 
print("conversao de fahrenheit para celsius")
temp = float(input("digite a temperatura em fahrenheit: "))
print(f"a conversao de {temp} fahrenfeit em celsius fica {5 * ((temp - 32)/9)}")