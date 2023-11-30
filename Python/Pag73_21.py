def main():
    stringa = "ciao"
    vocali = "aeiouAEIOU"
    nocons = " ".join([c for c in stringa if c not in vocali])
    print(stringa)
    print(nocons)

if __name__ == "__main__":
    main()
