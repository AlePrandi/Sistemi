def main():
    for numero in range(1, 1000):
        if sum([int(c)**3 for c in str(numero)]) == numero:
            print(f"Il numero '{numero}' è narcisista")
        
if __name__ == '__main__':
    main()