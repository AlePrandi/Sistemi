def convMask(el):
    group1 = int(el[0:8], 2)
    group2 = int(el[8:16], 2)
    group3 = int(el[16:24], 2)
    group4 = int(el[24:], 2)
    lista = [group1, group2, group3, group4]
    lista = [str(i) for i in lista]
    return ".".join(lista)
    
def main():
    ip_address=["192.168.222.0/27","192.168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    separatore = '/'
    mask = []
    for element in ip_address:
        indice = element.find(separatore)
        mask.append(int(element[indice + 1:]))
    mask_bin = ["1" * group + "0" * (32 - group) for group in mask]
    mask_dec = [convMask(group) for group in mask_bin]
    for k, element in enumerate(ip_address):
            print(f"la subnet mask di {element} è {mask_dec[k]}")
    
if __name__ == "__main__":
    main()