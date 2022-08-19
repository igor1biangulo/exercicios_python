"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
print("valida se e m ou f")
val = input("digite [f] ou [m]: ")
if val == "f":
    print("feminino")
if val == "m":
    print("masculilo")
else:
    print("vc n digitou nem uma das opçoes")