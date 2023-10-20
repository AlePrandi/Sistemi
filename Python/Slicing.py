# SLICING DI STRINGHE
s = "ciao come stai ?"
#     0123
#    -4-3-2-1 L'ULTIMO CARATTERE HA SEMPRE INDICE -1

print(f"il primo carattere e {s[0]}")
print(f"l'ultimo carattere e {s[-1]}")
print(f"l'ultimo carattere e {s[len(s)-1]}")  # C-style Da non usare
print(s[3:7])  # stampa tutto quello incluso tra la cella 3 e la cella 7
print(s[1:-1])  # stampa tutto esclusi il primo e l'ultimo carattere
print(s[1:])  # stampa tutto escluso il primo carattere
print(s[:-1])  # stampa tutto escluso l'ultimo carattere
print(s)  # stampa tutta la stringa
print(s[::-1])  # stampa la stringa invertita
