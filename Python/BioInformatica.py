def leggiFile(file):
    file = open(file, 'r')
    righe = file.readlines()
    nA, nC, nT, nG = 0, 0, 0, 0
    stringa = ""
    sequenza = "ATGTTTGTTTTT"
    
    for riga in righe:
        stringa = stringa + riga[: -1] 
        for char in riga:
            if char == "A":
                nA += 1
            if char == "T":
                nT += 1
            if char == "C":
                nC += 1
            if char == "G":
                nG += 1
    
    print(stringa)     
                
    for i, c in enumerate(stringa[:-12]):
        if stringa[i: i + 12] == sequenza:
            print(f"Sequenza trovata in posizione: {i}")        
                
    print(f"Adenina = {nA}")
    print(f"Citosina = {nC}")
    print(f"Timina = {nT}")
    print(f"Guanina = {nG}")
 
    file.close()
        
def main():
    
    nomefile = "covid-19_gen1.txt"
    leggiFile(nomefile)
    
if __name__ == "__main__":
    main()