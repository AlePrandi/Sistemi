import ipaddress

def main():
    ip_address=["192.168.222.0/27","192.168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    ip_mask = [ipaddress.IPv4Interface(group).with_netmask for group in ip_address]
    #print('.'.join(subnet_mask_bin[i: i+ 8] for i in range(0, 32, 8)))
    with open("mask.txt", "w") as f:
        for element in ip_mask:
            f.write(element[element.find("/") + 1:] + '\n')
    
if __name__ == "__main__":
    main()