from cryptography.fernet import Fernet
from main import KEY

def encrypt(message):
    f = Fernet(KEY)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message