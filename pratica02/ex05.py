"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
print("veja se vc foi aprovado")
nota = float("ditite nota um: ")
nota1 = float("ditite nota dois: ")
media = (nota + nota1)/2
if media >= 7:
    print("aprovado")
if media == 10:
    print("aprovado com distinçao")
else:
    print("reprovado")

