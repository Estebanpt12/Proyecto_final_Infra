from cryptography.fernet import Fernet

# Ejemplo de uso
clave = "YFLP_NMQpMp4wTw50i5_94V_VSYyqVJ_VL9r13ak6cQ="
texto_original = "143229910"

def encrypt_text(text):
    # No vuelvas a definir clave, accede a la variable global
    cipher_suite = Fernet(clave.encode())

    # Cifra el texto
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text):
    # No vuelvas a definir clave, accede a la variable global
    cipher_suite = Fernet(clave.encode())

    # Descifra el texto cifrado
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

# Cifrar el texto
##texto_cifrado = encrypt_text(texto_original)
##print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
##texto_descifrado = decrypt_text(texto_cifrado)
##print("Texto descifrado:", texto_descifrado)
