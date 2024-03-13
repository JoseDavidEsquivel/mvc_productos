function validarFormulario() {
    var precio = document.getElementById('precio').value;
    var existencias = document.getElementById('existencias').value;
    console.log(precio)
    var inputArchivo = document.getElementById('imagen');
    var archivo = inputArchivo.files[0];
    var tamanoMaximo = 1024 * 1024; // 1MB

    if (precio < 0 || existencias < 0) {
        alert('Los valores negativos en los campos de precio y existencias no son permitidos.');
        return false;
    }

    if (archivo && archivo.size > tamanoMaximo) {
        alert('El tamaño de la imagen excede el límite permitido (1MB).');
        inputArchivo.value = ''; // Borrar el archivo seleccionado
        return false;
    }
    return true;
}