from PyPDF2 import PdfReader

ruta_pdf = 'hola1.pdf'

try:
    with open(ruta_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)

        # Buscar el diccionario raíz (Root) del documento
        root = pdf_reader.trailer["/Root"]

        # Verificar si hay un formulario (AcroForm)
        if "/AcroForm" in root:
            acro_form = root["/AcroForm"]

            # Verificar si hay campos en el formulario
            if "/Fields" in acro_form:
                fields = acro_form["/Fields"]

                # Revisar cada campo
                found = False
                for field in fields:
                    field_obj = field.get_object()
                    if field_obj.get("/FT") == "/Sig":
                        print("✅ Firma digital encontrada en el campo del formulario.")
                        found = True
                        break

                if not found:
                    print("🚫 No hay firmas digitales en los campos del formulario.")
            else:
                print("🟡 El formulario no tiene campos definidos.")
        else:
            print("🚫 El PDF no tiene un formulario de firma (/AcroForm).")

except Exception as e:
    print(f"⚠️ Error al analizar el PDF: {e}")
