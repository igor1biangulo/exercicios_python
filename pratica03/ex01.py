"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
print("numero e valido??")
i = 1
while True:   
    num = input("digite um numero: ")
    if num.isnumeric():
        num = int(num)
     
        if num >= 0 and num <=10:
            print("seu numero e valido")
            break
        else:
            print(f"vamos tentar de novo, vc tentou {i} vezes")
            i += 1
          

            
          

