import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Ejemplo de uso
clave = "uniquindio_#2023".encode('utf-8')
iv = "1232123156789012".encode('utf-8')

def encrypt_text(data):
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_text(data):
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    ciphertext = cipher.decrypt(base64.b64decode(data.encode('utf-8')))
    plaintext = unpad(ciphertext, AES.block_size)
    return plaintext.decode('utf-8')

# Cifrar el texto
#texto_cifrado = encrypt_text("1007077423")
#print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
#texto_descifrado = decrypt_text("+Ehnn3DZjTQg7CnakgduKQ==")
#print("Texto descifrado:", texto_descifrado)
