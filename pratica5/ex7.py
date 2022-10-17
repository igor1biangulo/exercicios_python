"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""
def linha():
    print("----------------------------------------------")
def valorpagamento(vp,da):

    multa = vp*0.03
    juros = vp*0.001*da
    if da > 0:
        return vp+multa+juros
    elif da == 0:
        return vp
    else:
        print("algo deu errado tente novamente")

while True:
    
    valor = float(input("valor da parcela: "))
    if valor == 0:
        print("acabou sua divida vlw flw")
        break
    dias = int(input("dias em atraso: "))
    
    valor_final = valorpagamento(valor,dias)

    print(f"\nrelatorio do dia e {valor_final:.2f}")
    linha()

    