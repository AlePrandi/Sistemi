import random

def main():
    movimenti = [random.choice([1, -1]) for _ in range(60 * 60 * 24 * 5)]
    somma = 0
    for i in movimenti:
        somma += i
        
    print(movimenti)
    print(somma)
        
if __name__ == '__main__':
    main()