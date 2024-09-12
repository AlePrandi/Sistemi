import socket as sck
import AlphaBot

"""
SSH: secure shell
"""

isRunning = True

t = AlphaBot.AlphaBot()

MY_ADDRESS = ("0.0.0.0", 8000)

s_server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s_server.bind(MY_ADDRESS)

comandi = {"f": t.forward, "b": t.backward, "l":t.left, "r": t.right}

def get_key_from_value(value):
    for k, v in comandi.items():
        if v == value:
            return k
    return None # se il valore non è presente nel dizionario
    
def main():

    global isRunning

    s_server.listen()

    conn, addr = s_server.accept()

    while isRunning:
        text = conn.recv(4096)
        
        if text.decode() == "help":
            conn.sendall(b"Forward -> f;x\nBackward -> b;x\nRight -> r;x\nLeft -> l;x\n")
            continue

        elif text.decode() == "exit":
            conn.sendall(b"EXIT")
            isRunning = False
            continue

        elif text.decode().count(";") > 1 or text.decode().count(";") == 0:
            conn.sendall(b"\nErrore << ;; >>\n")
            continue

        elif get_key_from_value(text.decode().split(";")[0].lower()) is None:
            conn.sendall(b"\nErrore << comando non presente >>\n")
            continue

        elif float(text.decode().split(";")[1]) < 0:
            conn.sendall(b"\nErrore << valore negativo >>\n")
            continue
    
        else :
            conn.sendall(b"<>")
            comandi[text.decode().split(";")[0].lower()] (float(text.decode().split(";")[1]))

    s_server.close()

if __name__=="__main__":
    main()