from cryptography.fernet import Fernet
import hashlib
import binascii

def generate(password):
    salt = b''
    temp = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=32)
    KEY = binascii.hexlify(temp).decode()
    return KEY

def encrypt(message):
    from main import KEY
    f = Fernet(KEY)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt(message):
    from main import KEY
    f = Fernet(KEY)
    decrypted_message = f.decrypt(message).decode()
    return decrypted_message
