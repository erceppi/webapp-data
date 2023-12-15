"""
Este módulo contiene la lógica principal de la aplicación web.
Descripción adicional sobre lo que hace el módulo y su propósito general.
Puedes incluir detalles sobre las funcionalidades, la estructura del código, etc.
"""
# pylint: disable=E0401
# Deshabilitar el error de importación de Pylint (E0401) para el módulo Flask

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    Ruta principal que renderiza el archivo 'index.html'.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """
    Ruta para manejar la carga (upload) de un archivo CSV.

    Realiza la validación del archivo CSV y procesa sus datos si es válido.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No se encontró ningún archivo CSV"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Archivo no seleccionado"})

    if file:
        try:
            # Leer el archivo CSV y procesar los datos
            stream = file.stream.read().decode("UTF8")
            data = [row.split(',') for row in stream.split('\n') if row.strip()]

            if not data:
                return jsonify({"error": "El archivo CSV está vacío"})

            headers = data[0]
            rows = data[1:]

            # Renderizar una tabla con los datos del CSV en 'table.html'
            return render_template('table.html', headers=headers, rows=rows)
        except Exception as e:
            # Manejar errores al procesar el archivo CSV
            return jsonify({"error": f"Error al procesar el archivo CSV: {str(e)}"})

if __name__ == '__main__':
    # Iniciar la aplicación Flask en modo debug
    app.run(debug=True)
