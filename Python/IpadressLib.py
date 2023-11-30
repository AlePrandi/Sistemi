import ipaddress


def main():
    ipv4 = input("inserisici un IPv4: ")
    subnet = input("inserisci una subnet in CDR(es. /24): ")
    ipv4pieno = ipv4 + subnet
    ip = ipaddress.ip_address(ipv4)

    if ip.is_private == True:
        print(f"L'IP è privato")
    else:
        print(f"L'IP è pubblico")

    if ip.is_loopback == True:
        print(f"L'IP è di loopback")

    iprete = ipaddress.IPv4Network(ipv4pieno, strict=False)
    if ipv4pieno == str(iprete):
        print(f"L'Ip è di rete")
    else:
        print(f"L'Ip di rete è {iprete}")

    host = list(iprete.hosts())
    print(f"Il primo Ip utilizzabile è {host[0]} {subnet}")
    print(f"L'ultimo Ip utilizzabile è {host[-1]} {subnet}")


if __name__ == "__main__":
    main()
