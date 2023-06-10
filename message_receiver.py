import socket
import threading
import utils
import b8zs
import warnings
warnings.simplefilter("ignore", UserWarning)

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
        
        b8zs_code, b8zs_graph = b8zs.convert_to_b8zs(data.decode('utf-8'))
        print('Código de linha B8ZS:', b8zs_code)


        print('Mensagem binária recebida:', data)
        # Convert binary message to text
        bin_msg = utils.convert_to_text(data.decode('utf-8'))
        print('Mensagem encriptada recebida:', bin_msg)
        # Decrypt message
        msg_decrypted = utils.decrypt(bin_msg)

        print('Mensagem recebida:', msg_decrypted)
        # Plot B8ZS graph
        b8zs.plot_b8zs(b8zs_graph)


# Start thread to receive messages
thread_recebimento = threading.Thread(target=receive_message)
thread_recebimento.start()

# Wait for keyboard input to exit the program
input("Pressione Enter para encerrar...")

# Close connection and socket
conection.close()
sock.close()