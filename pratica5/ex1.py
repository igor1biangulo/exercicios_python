"""  
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n"""
def funcao(n):
    for i in range(n):
        i += 1 
        print( str(i) * i)

funcao(4)


