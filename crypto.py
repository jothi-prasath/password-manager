from cryptography.fernet import Fernet
import hashlib
import base64

def generate(password):
    key = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key)
    return fernet_key

def encrypt(message,KEY):
    f = Fernet(KEY)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt(message,KEY):
    f = Fernet(KEY)
    decrypted_message = f.decrypt(message).decode()
    return decrypted_message
