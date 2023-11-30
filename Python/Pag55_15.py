def main():
    nome = str(input("inserire un nome: "))
    nome = nome[0] + '*' * (len(nome) - 1)
    print(f"Nome con prima lettera: {nome}")

if __name__ == "__main__":
    main()