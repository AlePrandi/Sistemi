import threading
import math

def isprimo(x):
    for i in range(x):
        if x % (i+1) == 0:
            return False
    return True

def main():
  n = 55
  for i in range(2, int(math.sqrt(n))+1):
        if isprimo(i):
            c = n // i
            if isprimo(c) and c!=i:
                print(f"{n} è formato dai numeri primi {c} e {i}")
            
if __name__ == "__main__":
    main()