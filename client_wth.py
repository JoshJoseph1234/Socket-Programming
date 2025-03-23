import socket

SERVER_IP = "127.0.0.1"
PORT = 12346

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((SERVER_IP, PORT))

print("[UDP Client] Listening for weather updates...")

while True:
    data, _ = udp_socket.recvfrom(1024)
    print(f"[UDP] Weather Update: {data.decode()}")
