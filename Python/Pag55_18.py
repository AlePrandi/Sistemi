def quadrati(num):
    return num*num

def main():
    num1 = int(input("inserire un numero: "))
    num2 = int(input("inserire un secondo numero: "))
    lista = [quadrati(num1) + quadrati(num2), quadrati(num1 + num2), quadrati(num1) - quadrati(num2), quadrati(num1 - num2)]
    print(lista)

if __name__ == "__main__":
    main()