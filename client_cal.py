import socket

SERVER_IP = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

expression = input("Enter math expression (e.g., 5+3*2): ")
client_socket.send(expression.encode())

result = client_socket.recv(1024).decode()
print(f"[TCP] Result: {result}")

client_socket.close()
