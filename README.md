# verificador-firmas
# Verificador de Firmas Digitales en PDF

Este proyecto permite verificar firmas digitales en archivos PDF utilizando un microservicio con Flask (Python) y una aplicación cliente con Node.js. 

## Requisitos previos

### Node.js

### Python
 (https://www.python.org/downloads/).

### Librerías y dependencias


####(Python - Flask):

1. **Flask**: Un framework web ligero para Python.
2. **pyHanko**: Librería para verificar firmas digitales en archivos PDF.
3. **PyPDF2**: Librería para manejar y leer archivos PDF.

#### (Node.js):

1. **axios**: Cliente HTTP para hacer solicitudes desde Node.js.
2. **form-data**: Paquete que facilita la creación de formularios multipart para cargar archivos.

## Instalación

### (Python)
1. **librerías necesarias**:

    ```
    pip install -r requirements.txt
    ```

2. **Inicia el servidor de Flask**:

    ```bash
    python validador_firma.py
    ```

    El servidor Flask correrá en el puerto `5001` de forma predeterminada.

### (Node.js)

1. **Instala las dependencias de Node.js**:

    ```
    npm install
    ```

2. **archivo PDF a verificar**:

    Cambia el nombre del archivo PDF en el script `verificador.js` (línea 6)-El archivo se tiene que subir en la raiz del proyecto:

    ```javascript
    const pdfPath = './hola.pdf'; // Cambia esto por el nombre real de tu archivo
    ```

3. **Ejecuta el script de verificación**:

    ```bash
    node verificador.js
    ```

    Esto enviará el archivo PDF al servidor Flask para validarlo.

## Descripción de los archivos

- **app.py**: El servidor Flask que maneja la validación de firmas digitales en los archivos PDF.
- **verificador.js**: El script en Node.js que envía el archivo PDF al servidor Flask y muestra la respuesta.
- **hello.pdf**: Un archivo PDF de ejemplo para la validación.

## Notas

- Asegurarse  que el servidor de Flask esté corriendo antes de ejecutar el script de Node.js.
Respuestas:
Si la firma es válida:
firma_valida: true

Si la firma no es válida:
firma_valida: false
Y adicionalmente:
INTACT: Si la firma es válida y el documento no ha sido modificado.

UNTRUSTED: Si la firma no se puede verificar porque el certificado no es confiable.

TIMESTAMP_TOKEN: Si la firma incluye un sello de tiempo.

EXTENDED_WITH_FORM_FILLING: Si la firma permite modificaciones en formularios.

ACCEPTABLE_MODIFICATIONS: Si el documento permite ciertos cambios después de la firma.
------
Hay un ejemplo básico también para validar que el documento PDF tiene una firma, hay que subir un PDf a la raiz del proyecto
Cambiar el nombre del archivo en `verificar_firma_basica.py` (línea 3):
 ```javascript
    ruta_pdf = 'hola1.pdf'
  ```
Despues correr  ```python verificar_firma_basica.py x consola.
Si tiene firma:
"Firma digital encontrada en el campo del formulario."
Si no:
"El PDF no tiene un formulario de firma (/AcroForm)."
