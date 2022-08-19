"""
Faça um Programa que leia três números e mostre-os em ordem decrescente
"""
print("entre tres numeros em ordem decrescente")
a = int(input("numero 1"))
b = int(input("numero 2"))
c = int(input("numero 3"))
if a > b and b > c:
    print(f"[{a},{b},{c}]")
elif b > a and a > c:
    print(f"[{b},{a},{c}]")
elif c > a and a > b:
    print(f"[{c},{a},{b}]")
elif b > c and c > a:
    print(f"[{b},{c},{a}]")
elif a > c and c > b:
    print(f"[{a},{c},{b}]")
elif c > b and b > a:
    print(f"[{c},{b},{a}]")

