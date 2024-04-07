import socket
import time


receiver_ip = '127.0.0.1'  
receiver_port = 12346  

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((receiver_ip, receiver_port))

start_time = time.time()
last_bit_time = start_time

secret_message = ''
start = True
while True:
    try:
        bit, _ = sock.recvfrom(1024) 
        bit = bit.decode()

        current_time = time.time()
        time_elapsed = current_time - last_bit_time 

        last_bit_time = current_time

        if not start: 
            if time_elapsed >= 0.5:  
                secret_message += '1'
            elif time_elapsed >= 0.25:  
                secret_message += '0' 
        start = False    
        print(f'secret message to this point : {secret_message}')


    except KeyboardInterrupt:
        break

# Close the socket
sock.close()
