# calcola ip di rete e ip di boradcast.

def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0" * (8 - l) + b

ipAddress = input("inserisci indirizzo ip: ")
# ipAddress_bin =
sub_num = int(input("inserisci subnet mask in CDR senza /: "))
sub_bin = "1" * sub_num + "0" * (32 - sub_num)
wild_bin = "0" * sub_num + "1" * (32 - sub_num)
lista = sub_num * "1" + "0" * (32 - sub_num)

group1 = int(lista[0:8], 2)
group2 = int(lista[8:16], 2)
group3 = int(lista[16:24], 2)
group4 = int(lista[24:], 2)

lista = [group1, group2, group3, group4]
lista = [str(elemento) for elemento in lista]  # converte la stringa in CDR in decimale

groups = ipAddress.split(".")  

groups = [int(group) for group in groups]  # convertire i gruppi da stringhe a interi
groups_b = [bin(elemento) for elemento in groups]
groups_strbin = [completa8bit(strbin) for strbin in groups_b]
ipAddress_bin = "".join(groups_strbin)

rete_str = [
    "1" if (a == "1" and b == "1") else "0" for a, b in zip(ipAddress_bin, sub_bin)
]
broad_str = [
    "1" if (a == "1" or b == "1") else "0" for a, b in zip(ipAddress_bin, wild_bin)
]

rete_bin = "".join(rete_str)
broad_bin = "".join(broad_str)

list_rete_bin = [rete_bin[i : i + 8] for i in range(0, 32, 8)]
list_broad_bin = [broad_bin[i : i + 8] for i in range(0, 32, 8)]

list_rete_dec = [int(group, 2) for group in list_rete_bin]
list_broad_dec = [int(group, 2) for group in list_broad_bin]

list_rete_dec = [str(elemento) for elemento in list_rete_dec]
list_broad_dec = [str(elemento) for elemento in list_broad_dec]

print("")
print(f"Ip rete: " + ".".join(list_rete_dec))
print(f"Ip broadcast: " + ".".join(list_broad_dec))
print(f"Subnet Mask: " + ".".join(lista))
print("")