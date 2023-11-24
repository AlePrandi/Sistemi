import ipaddress

def main():
    ipv4 = input("inserisici un IPv4 di rete: ")
    subnet = input("inserisci una subnet senza CDR: ")
    
    if ipaddress.ip_address(ipv4).is_private == True:
        print(f"L'IP è privato")
    
    if ipaddress.ip_address(ipv4).is_loopback == True:
        print(f"L'IP è di loopback")
        
    print(list(ipaddress.ip_network(ipv4).hosts()))
        
if __name__ == '__main__':
    main()