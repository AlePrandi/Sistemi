import hashlib


def main():
    
    m = hashlib.sha256()

    m.update(input("Inserisci una frase: ").encode())

    print(f"digest della frase: {m.hexdigest()}")

    file = "../Istruzioni_Encapsulation.txt"

    m.update(open(file, 'br').read())
    print(f"digest del file: {m.hexdigest()}")
    
if __name__ == '__main__':
    main()