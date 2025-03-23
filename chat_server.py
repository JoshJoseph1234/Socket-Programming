import socket
import threading

# Server configuration
HOST = "0.0.0.0"
TCP_PORT = 5555
UDP_PORT = 5556

# Handles TCP connections
def handle_tcp_client(client_socket, addr):
    print(f"[NEW TCP CONNECTION] {addr} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[TCP] {addr}: {message}")
            client_socket.send(f"Server (TCP) received: {message}".encode())
        except:
            break
    print(f"[TCP DISCONNECTED] {addr} disconnected.")
    client_socket.close()

# Handles UDP messages
def handle_udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, UDP_PORT))
    print(f"[UDP SERVER] Listening on {UDP_PORT}...")
    
    while True:
        message, addr = udp_socket.recvfrom(1024)
        print(f"[UDP] {addr}: {message.decode()}")
        udp_socket.sendto(f"Server (UDP) received: {message.decode()}".encode(), addr)

# Start TCP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, TCP_PORT))
tcp_socket.listen(5)
print(f"[TCP SERVER] Listening on {TCP_PORT}...")

# Start UDP server thread
udp_thread = threading.Thread(target=handle_udp_server, daemon=True)
udp_thread.start()

# Accept TCP clients
while True:
    client_socket, addr = tcp_socket.accept()
    client_thread = threading.Thread(target=handle_tcp_client, args=(client_socket, addr))
    client_thread.start()
