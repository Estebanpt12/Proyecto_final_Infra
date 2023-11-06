<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Conectarse a la base de datos (debes completar los datos de conexión).
    $conn = new mysqli("localhost", "usuario", "contraseña", "basededatos");

    if ($conn->connect_error) {
        die("Error de conexión a la base de datos: " . $conn->connect_error);
    }

    // Consultar la base de datos para verificar las credenciales.
    $query = "SELECT * FROM personas WHERE username = '$username' AND password = '$password'";
    $result = $conn->query($query);

    if ($result->num_rows > 0) {
        // Usuario autenticado
        $row = $result->fetch_assoc();
        echo "¡Bienvenido, " . $row["nombre"] . " " . $row["apellido"] . "!";
    } else {
        echo "Usuario no encontrado o contraseña incorrecta.";
    }

    $conn->close();
}
?>
