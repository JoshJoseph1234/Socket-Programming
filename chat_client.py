import socket

SERVER_IP = "127.0.0.1"
TCP_PORT = 5555
UDP_PORT = 5556

def tcp_chat():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, TCP_PORT))
    
    print("[CONNECTED TO TCP SERVER]")
    while True:
        message = input("You (TCP): ")
        if message.lower() == "exit":
            break
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(response)
    
    client.close()

def udp_chat():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print("[CONNECTED TO UDP SERVER]")
    while True:
        message = input("You (UDP): ")
        if message.lower() == "exit":
            break
        client.sendto(message.encode(), (SERVER_IP, UDP_PORT))
        response, _ = client.recvfrom(1024)
        print(response.decode())
    
    client.close()

# User chooses TCP or UDP
print("Choose mode: 1) TCP  2) UDP")
choice = input("Enter choice (1/2): ").strip()

if choice == "1":
    tcp_chat()
elif choice == "2":
    udp_chat()
else:
    print("Invalid choice. Exiting.")
