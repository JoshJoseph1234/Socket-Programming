import socket

HOST = "0.0.0.0"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"[TCP Server] Listening on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[TCP] Client connected from {addr}")

    expression = client_socket.recv(1024).decode()
    print(f"[TCP] Received: {expression}")

    try:
        result = str(eval(expression))  # Calculate result
    except:
        result = "Invalid expression"

    client_socket.send(result.encode())
    client_socket.close()
