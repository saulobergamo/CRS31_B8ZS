import socket
import threading

# Configure the IP address and port of the target computer
foreign_ip = '192.168.0.186'  # IP do Computador 2
foreign_port = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to target computer
sock.connect((foreign_ip, foreign_port))

def send_message():
    while True:
        # Send message
        msg = input('Digite uma mensagem: ')
        sock.sendall(msg.encode('utf-8'))

# Start thread to send messages
send_thread = threading.Thread(target=send_message)
send_thread.start()

while True:
    # Receive message
    data = sock.recv(1024)
    if not data:
        break
    msg_received = data.decode('utf-8')
    print('Mensagem recebida:', msg_received)

# Close socket
sock.close()