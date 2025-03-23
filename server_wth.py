import socket
import random
import time

HOST = "0.0.0.0"
PORT = 12346

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))

print(f"[UDP Server] Broadcasting weather updates on port {PORT}...")

while True:
    temperature = random.uniform(20, 35)
    humidity = random.uniform(40, 60)
    weather_update = f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%"
    
    udp_socket.sendto(weather_update.encode(), ("127.0.0.1", PORT))  # Broadcast to local clients
    time.sleep(2)
