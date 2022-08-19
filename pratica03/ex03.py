"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""



print("validando informaçoes")
def linha():
    print("---------------------------------")
m = []
x = ["nome", "idade","salario","sexo","estado civil"]

linha()

while True:
    nome = input("digite seu nome: ")
    if len(nome) >= 3:
        print("nome valido")
        m.append(nome)
        break
    else:
        print("nome tem que ter no minimo de 3 letras")
linha()
while True:
    idade = input("digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade <= 150:
            print("idade valido")
            m.append(idade)
            break

        else:
            print("uma pessoa com mais de 150 anos e meio dificio ne.")
    else:
        print("somente numero podem ser validados")
linha()
while True:
    salario = float(input("digite seu salario: "))
    if salario == round(salario):
        salario = int(salario)
        if salario > 0:
            print("salario valido")
            m.append(salario)
            break
        else:
            print("salario tem que ser maior que zero")
    elif not salario == round(salario):
         if salario > 0:
            print("salario valido")
            m.append(salario)
            break
         else:
            print("salario tem que ser maior que zero")
        
    else:
        print("somente numero podem ser validados")

linha()
while True:
    sexo = input("digite seu sexo [f]feminino [m]masculino: ")   
    if sexo == "f" or sexo == "m" :
        print("sexo valido")
        m.append(sexo)
        break
    else:
        print("vc e masculino ou feminino")
linha()
while True:
    etd = input("digite seu estado civil [s]solteiro, [c]casado, [v]vilvo, [d]divorciado: ")   
    if etd == "s" or etd == "v" or etd == "d" or etd == "c":
        print("estado civil valido")
        m.append(etd)
        break
    else:
        print("digite alguma das opçoes")
linha()

for i in range(0,5):
    print(f"{x[i]}: {m[i]}")








