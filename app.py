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
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No se encontró ningún archivo CSV"})

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Archivo no seleccionado"})

        data = []
        try:
            stream = file.stream.read().decode("UTF8")
            data = [row.split(',') for row in stream.split('\n') if row.strip()]

            if not data:
                return jsonify({"error": "El archivo CSV está vacío"})

            headers = data[0]
            rows = data[1:]
            return render_template('table.html', headers=headers, rows=rows)

        except UnicodeDecodeError as e:
            return jsonify({"error": f"Error: No se pudo decodificar el archivo - {str(e)}"}), 400

        except FileNotFoundError as e:
            return jsonify({"error": f"Error: Archivo no encontrado - {str(e)}"}), 400

        except Exception as e:
            return jsonify({"error": f"Error al procesar el archivo CSV: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"Error inesperado al manejar la solicitud: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
