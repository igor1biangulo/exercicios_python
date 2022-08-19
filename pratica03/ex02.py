"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
def dec():
    not nome == senha and nome.isalpha() and senha.isalnum() or senha.isalpha() and len(nome) > 3 and len(senha) > 8
    
print("nome e usuario n pode ser iguais")
cond = 0

while True:
    while cond == 0:
        print("nome tem que ter 8 digito e ter somente letras\nsenha tem que ter 8 digitos")
        nome = input("nome: ")
        senha = input("senha: ")
        if not nome == senha and nome.isalpha() and senha.isalnum() or senha.isalpha() and len(nome) > 3 and len(senha) > 8:
            print("login perfeito")
            break

        elif not dec():
            print("login invalido, confira os dados ")
            cond += 1

    while cond > 1:
        print("tente mais uma vez so que coloque os dados certos")
        print("nome tem que ter 8 digito e ter somente letras\nsenha tem que ter 8 digitos")
        nome = input("nome: ")
        senha = input("senha: ")
        if not nome == senha and nome.isalpha() and senha.isalnum() or senha.isalpha() and len(nome) > 3 and len(senha) > 8:
            print("login perfeito")
            break

        elif not nome == senha and not nome.isalpha() and not senha.isalnum() or not senha.isalpha() and  not len(nome) > 3 and not len(senha) > 8:
            print("login invalido, confira os dados ")
            cond += 1
    
    

