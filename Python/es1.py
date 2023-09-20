def main():
    #per eseguire il programma andare su cmd -> cd C:\Users\Paolo\Desktop\SCUOLA\SISTEMI\Python e pois si lancia python nome.py
    nome = input ("Come ti chiami ?") #input ritorna solo stringhe
    anni = int(input ("Quanti anni hai?"))
    annoAtt = int(input ("In quale anno siamo ?"))
    print(f"Il tuo nome è {nome} e sei nato nel {annoAtt- anni}")
    #type(nomeVariabile) per visualizzare il tipo della variabile
if __name__ == "__main__":
    main()          #scrivere sempre per far funzionare il main