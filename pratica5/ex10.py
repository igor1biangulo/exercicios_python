"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
import random 
import time

def jogo():
    cont = 0
    care = ["=="]
    pontos = 0
    while True:
        cont += 1
        print(cont)
        valor = random.randint(1,6)
        valor2 = random.randint(1,6)
        soma_dos_dados = valor+valor2
        for i in range(5):
            print(*care)
            care.append("==")
            time.sleep(0.7)
        care.clear()
        print(f"seus dados deram {soma_dos_dados}")
        if cont == 1:
            if soma_dos_dados == 7 or soma_dos_dados == 11:
                print("vc ganhou")
                break
            if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                print("deu crash perdeu ")
                break
            else:

                pontos += soma_dos_dados

        elif cont>0:
            if soma_dos_dados == 7:
                print("vc perdeu") 
                break
         
            if pontos == soma_dos_dados:
                print(f"numero de pontos da primeiro rodada e iqual a esta jogada, vc ganhou")
                break
    print("ate mais")

print(jogo())

                

                

        
        

    




