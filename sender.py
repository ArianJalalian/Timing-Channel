import socket
import time


receiver_ip = '127.0.0.1' 
receiver_port = 12346  

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

secret_message = '1010101'  
data = b'A'  

for char in data:
    binary_char = bin(char)[2:].zfill(8)

    for i, bit in enumerate(binary_char):
        sock.sendto(bit.encode(), (receiver_ip, receiver_port)) 
        if i == len(secret_message):
            continue 
        delay = 0.5 if secret_message[i] == '1' else 0.25
        time.sleep(delay)

sock.close()
