# List_comprehension
# riempire le liste facilmente

import random

quadrati = [i * i for i in range(1, 6)]  # quadrati di i da 0 a 5

numeri_interi = [i for i in range(1, 11)] # numeri da 0 a 10

stringhe = ["computer", "cellulare", "laptop"]

stringhe_c = [parola for parola in stringhe if parola[0] == "c"] 
# parole in stringhe che iniziano con la c

voti = [random.randint(2,10) for _ in range(0, 10)] # _ per variabili che non usiamo

voti_insuff = [ voto for voto in voti if voto < 6 ]

#print(quadrati)
#print(numeri_interi)
#print(stringhe_c)
print(voti)