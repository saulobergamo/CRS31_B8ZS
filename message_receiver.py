import socket
import threading

# Configure the IP address and port of the local computer
local_ip = '192.168.0.186'  # Local computer IP address
local_port = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to local port
sock.bind((local_ip, local_port))

# Wait for incoming connections
sock.listen(1)

print('Aguardando por conexões...')

# Accept incoming connection
conection, address = sock.accept()
print('Conexão estabelecida de:', address)

def receive_message():
    while True:
        # Receive message
        data = conection.recv(1024)
        if not data:
            break
        msg_received = data.decode('utf-8')
        print('Mensagem recebida:', msg_received)

# Start thread to receive messages
thread_recebimento = threading.Thread(target=receive_message)
thread_recebimento.start()

# Wait for keyboard input to exit the program
input("Pressione Enter para encerrar...")

# Close connection and socket
conection.close()
sock.close()