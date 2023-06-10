import socket
import threading
import b8zs
import utils

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

        # Crypt message
        crypt_msg = utils.encrypt(msg)
        print('Mensagem criptografada:', crypt_msg)
        # Convert message to binary
        binary_message = utils.convert_to_binary(crypt_msg)
        print('Mensagem em binário:', binary_message)
        # Convert binary message to B8ZS
        b8zs_code, b8zs_graph = b8zs.convert_to_b8zs(binary_message)
        print('Código de linha B8ZS:', b8zs_code)
        # Plot B8ZS graph
        b8zs.plot_b8zs(b8zs_graph)
        
        sock.sendall(binary_message.encode('utf-8'))

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