from flask import Flask, request, jsonify
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.sign.fields import SigFieldSpec
from pyhanko.pdf_utils.reader import PdfFileReader
import io

app = Flask(__name__)

@app.route('/validar', methods=['POST'])
def validar_pdf():
    try:
        file = request.files['pdf']
        
        if not file:
            return jsonify({
                'firma_valida': False,
                'mensaje': 'No se ha recibido un archivo PDF.',
            })
        
        pdf_bytes = file.read()
        
        if len(pdf_bytes) == 0:
            return jsonify({
                'firma_valida': False,
                'mensaje': 'El archivo PDF está vacío.',
            })

        pdf_stream = io.BytesIO(pdf_bytes)
        reader = PdfFileReader(pdf_stream)

        # Verificar AcroForm
        if not reader.root.get("/AcroForm"):
            return jsonify({
                'firma_valida': False,
                'mensaje': 'El archivo PDF no contiene formularios ni firmas.'
            })

        # Guarda las firmas antes de resetear
        signatures = list(reader.embedded_signatures)

        # Reinicia el stream para que validate_pdf_signature lo pueda leer
        pdf_stream.seek(0)


        if not signatures:
            return jsonify({
                'firma_valida': False,
                'mensaje': 'El archivo PDF no contiene firmas incrustadas.'
            })

        resultados = []
        for sig in signatures:
            try:
                result = validate_pdf_signature(sig)
                resultados.append({
                    'valida': result.valid,
                    'mensaje': str(result.summary()) 
                })
            except Exception as e:
                resultados.append({
                    'valida': False,
                    'mensaje': f'Error al validar firma: {str(e)}'
                })

        return jsonify({
            'firma_valida': any(r['valida'] for r in resultados),
            'detalles': resultados
        })

    except Exception as e:
        return jsonify({
            'firma_valida': False,
            'mensaje': f'Error general: {str(e)}'
        })

if __name__ == '__main__':
    app.run(port=5001)
