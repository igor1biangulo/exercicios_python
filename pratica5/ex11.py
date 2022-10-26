"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
def extrenso_mes(dia,mes,ano):
     meses = [" ","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezenbro"]

     if dia <=31:
          mes = meses[mes]
          if dia >28 and mes=="fevereiro" and ano %4==2 :
               return "esse dia n tem nesse ano ele e bisesto"

          elif mes == "fevereiro" and dia >=30:
               return "fevereiro so tem 29 ou28 dias"
               

          else:
               return f"{dia} de {mes} do ano {ano}"

     else:

          return "data invalida "


data = input("digite a data: ")
 
lista = data.split("/")
dat_list = [int(v) for v in lista]
d = dat_list[0]
m = dat_list[1]
a = dat_list[2]
resulto=extrenso_mes(d, m, a)
print(resulto)








          




 
           