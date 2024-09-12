import socket as sck

SERVER_ADDRESS = ("192.168.1.146",8000)
BUFFER_SIZE = 4096

def client():
    s_client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s_client.connect(SERVER_ADDRESS)

    print("Connected to server at", SERVER_ADDRESS)

    try:
        while True:
            command = input("Enter command (type 'help' for commands, 'exit' to quit): ")

            if command == "exit":
                s_client.sendall(command.encode())
                response = s_client.recv(BUFFER_SIZE)
                print("Server:", response.decode())
                break

            s_client.sendall(command.encode())
            response = s_client.recv(BUFFER_SIZE)
            print("Server:", response.decode())

    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        s_client.close()
        print("Connection closed.")

if __name__ == "__main__":
    client()
