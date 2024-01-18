'''
utilizzare le code usando la push() e la pop(0) 
'''

def Enqueue(coda, valore):
    coda.append(valore)
    
def Dequeue(coda):
    coda.pop(0)
    

def main():
    coda = [1 , 2 , 3 , 4 , 5]
    print(coda)
    num = 7
    Enqueue(coda, num)
    print(coda)
    Dequeue(coda)
    print(coda)
    
if __name__ == "__main__":
    main()