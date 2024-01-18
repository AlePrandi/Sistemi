lettere = "abcdefghijklmnopqrstuvwxyz ?!"
lett2num = {}
num2lett = {}
for posizione, lettera in enumerate(lettere):
    num2lett[posizione] = lettera 
    lett2num[lettera] = posizione
    
testo_chiaro = input("Inserisci una stringa: ")
chiave = "itisdelpozzoqwretrytuygihijdnvaioghqerbv"
testo_criptato = ""

#codifica
for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
    numero = (lett2num[lettera_testo] + lett2num[lettera_chiave]) % len(lettere)
    testo_criptato = testo_criptato + num2lett[numero]
print(f"il testo '{testo_chiaro}' diventa '{testo_criptato}'.")

testo_chiaro = ""

#decodifica
for lettera_testo, lettera_chiave in zip(testo_criptato, chiave):
    numero = (lett2num[lettera_testo] - lett2num[lettera_chiave]) % len(lettere)
    testo_chiaro = testo_chiaro + num2lett[numero]
print(f"il testo '{testo_criptato}' è tornato '{testo_chiaro}'.")