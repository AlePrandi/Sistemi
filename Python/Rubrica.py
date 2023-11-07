def main():
    dizionario = {} 
    fp =  open('Rubrica.txt', 'r')
    righe = fp.readlines()
    
    for riga in righe:
        campi = riga.split(', ') #strip toglie \n
        nome = campi[0]
        numero = int(campi[1].replace('\n', ''))
        dizionario[nome] = numero
        
    for chiave in dizionario:
        print(f"{chiave}: {dizionario[chiave]}")
        
    fp.close()
    
if __name__ == "__main__":
    main()