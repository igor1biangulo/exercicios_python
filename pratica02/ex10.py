"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print("que horario vc estuda")
hr = input("turnos [M] matutino [v] vespertino [n] noturno\ndigite a opçao: ")
if hr=="m":
    print("bom dia")
elif hr=="v":
    print("boa tarde")
elif hr=="n":
    print("boa noite")
else:
    print("digite uma opçao valida,boco")