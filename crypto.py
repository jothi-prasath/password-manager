from cryptography.fernet import Fernet
from main import KEY

def encrypt(message):
    f = Fernet(KEY)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt(message):
    f = Fernet(KEY)
    decrypted_message = f.decrypt(message).decode()
    return decrypted_message