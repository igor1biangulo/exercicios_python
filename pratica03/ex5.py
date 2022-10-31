"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""


import re
import os
from time import sleep

os.system("cls")

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

def is_number(val):
    return is_int(val) or is_float(val)

while True:

    pois_a = input(f"\033[34m pais A : \033")
    taxa_a = input(f"\033[34m texa de crescimento : \033")
    if pois_a.isnumeric() and is_number(taxa_a):
        pois_b = input(f"\033[34m pais B : \033")
        taxa_b = input(f"\033[34m texa de crescimento : \033")
        if pois_b.isnumeric() and is_number(taxa_b):
            pois_a,pois_b = int(pois_a),int(pois_b)
            taxa_a,taxa_b = float(taxa_a), float(taxa_b)
            break
    
    print("\33[34m tente novamente")
    sleep(0.7)
    os.system("cls")
anos = 0
while True:
    cal_a = pois_a*(taxa_a/100)
    pois_a = pois_a + cal_a
    cal_b = pois_b*(taxa_b/100)
    pois_b = pois_b + cal_b
    anos += 1
    if pois_a > pois_b:
        break

print(f"\033[35m depois de",f"\033[34m{anos} anos\033")