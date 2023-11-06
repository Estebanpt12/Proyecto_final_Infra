document.getElementById("consultar").addEventListener("click", function() {
    // Contenido que deseas codificar en el código QR (por ejemplo, una URL):
    const contenido = "https://www.ejemplo.com";

    // Genera el código QR y muéstralo en el elemento con id "codigo-qr":
    const qrCode = new QRCode(document.getElementById("codigo-qr"), {
        text: contenido,
        width: 128,
        height: 128
    });

    // Muestra el enlace de descarga:
    document.getElementById("descargar").style.display = "block";
});

document.getElementById("descargar").addEventListener("click", function() {
    // Datos de usuario y contraseña que deseas enviar al servidor
    const usuario = "tu_usuario";
    const contraseña = "tu_contraseña";

    // Realiza una solicitud HTTP al servidor local en el puerto 8080
    // para obtener el código QR, aquí asumimos que el servidor devuelve
    // el código QR como una imagen en formato PNG
    fetch(`http://localhost:8080/obtenerCodigoQR?usuario=${usuario}&contraseña=${contraseña}`)
        .then(response => response.blob())
        .then(blob => {
            // Crea un enlace de descarga
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = "codigo_qr.png";

            // Simula un clic en el enlace para iniciar la descarga
            a.click();
        })
        .catch(error => {
            console.error("Error al obtener el código QR:", error);
        });
});

