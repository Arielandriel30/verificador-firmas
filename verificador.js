const fs = require('fs');
const axios = require('axios');
const FormData = require('form-data');

// Ruta al archivo PDF a verificar
const pdfPath = './hola.pdf'; 

const form = new FormData();
form.append('pdf', fs.createReadStream(pdfPath));

// Envia el PDF al servidor Flask
axios.post('http://127.0.0.1:5001/validar', form, {
  headers: form.getHeaders()
})
.then(response => {
  console.log('Respuesta del validador:', response.data);
})
.catch(error => {
  if (error.response) {
    console.error('Error del validador:', error.response.data);
  } else {
    console.error('Error en la petición:', error.message);
  }
});
