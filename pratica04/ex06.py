"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
listaNotas = []
acima_da_media =[]
soma = 0
con = 0

def linha():
    print(f"---------------------------------------")
print ('Notas dos Alunos')
for i in range(3):
    nome = input("digite seu nome: ")
    for v in range(0,4):
        nota = 0
        nota += float(input(f"nota "+str(v+1)+": ")) 
        listaNotas.append(nota)
        media = sum(listaNotas)/4
    if media >=7:
        con += 1   
        acima_da_media.append(nome) 
    linha()
    
for x in range(con):
    print(f"{acima_da_media[x]}")




       

    
    