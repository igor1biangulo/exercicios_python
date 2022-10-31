"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""
pois_a = 80000
pois_b = 200000
taxa_a = 0.03
taxa_b = 0.015
anos = 0
while True:
    cal_a = pois_a*taxa_a
    pois_a = pois_a + cal_a
    cal_b = pois_b*taxa_b
    pois_b = pois_b + cal_b
    anos += 1
    if pois_a > pois_b:
        break

print(anos)
