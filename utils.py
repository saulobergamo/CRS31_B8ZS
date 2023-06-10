def encrypt(message):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + 1)  # Encrypts the message by adding 1 to the ASCII value of each character
    return encrypted_message

def convert_to_binary(message):
    binary_message = ""
    for char in message:
        binary_message += format(ord(char), '08b')  # Converts each character to its 8-bit binary value
    return binary_message

def decrypt(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - 1)  # Decrypts the message by subtracting 1 from the ASCII value of each character
    return decrypted_message

def convert_to_text(binary_message):
    text_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        text_message += chr(int(byte, 2))  # Converts each 8-bit binary byte to its corresponding character
    return text_message

