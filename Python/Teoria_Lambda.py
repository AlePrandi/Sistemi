#Lambda utile per definire funzioni brevi

#no Lambda
def somma(a, b):
    return a+b

#lamda
somma1 = lambda x,y : x + y

lista = [10,4]
print(somma1(lista[0],lista[1]))# metodo classico

print(somma1(*lista))# lista spacchettata sui parametri 