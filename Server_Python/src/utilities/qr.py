import qrcode
import os

#db.auth("nombre_de_usuario_admin", "contraseña_admin")

def generar_codigo_qr(texto, ruta_destino):
    qr = qrcode.QRCode(
        version=1,  # Versión del código QR
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L: bajo)
        box_size=10,  # Tamaño de cada celda en el código QR
        border=4,  # Margen del código QR
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(ruta_destino)

# Ejemplo de uso
texto_a_codificar = "gAAAAABlPceSUmuy2tsTlZAoKNn2mYnIa7KPS3ZPZgTUW1zOTRvsBeokqrvcCxDI1O7sNViLWDiFfGna5mWRYdX3YSDl_cBJ_g=="
ruta_destino_qr = "/home/esteban/Documents/U/Infra/Proyecto_final_Infra/Server_Python/src/images/codigo_qr.png"

generar_codigo_qr(texto_a_codificar, ruta_destino_qr)
print(f'Se ha generado el código QR en el archivo "{ruta_destino_qr}"')
