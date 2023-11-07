import qrcode

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
