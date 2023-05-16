from cryptography.fernet import Fernet
import hashlib
import base64

def generate(password):
    # converts 'password' into bytes and calculates the sha256 hash, 
    # returns hash value as bytes object
    key = hashlib.sha256(password.encode()).digest()
    # encode the key into base64 encoded string
    fernet_key = base64.urlsafe_b64encode(key)
    return fernet_key

def encrypt(message,KEY):
    f = Fernet(KEY)
    # converts the message into bytes and encrypt using the key
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt(message,KEY):
    f = Fernet(KEY)
    # decrypts the message using the key and converting bytes into string
    decrypted_message = f.decrypt(message).decode()
    return decrypted_message
