from flask import Flask, render_template, request, jsonify
import io
import csv

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

        try:
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_data = csv.reader(stream)
            data = list(csv_data)

            if not data:
                return jsonify({"error": "El archivo CSV está vacío"})

            # Procesamiento especial para unir campos con comas dentro de comillas dobles
            for row in data:
                for i, cell in enumerate(row):
                    if cell.startswith('"') and cell.endswith('"'):
                        while not cell.endswith('"') and i + 1 < len(row):
                            i += 1
                            cell += ',' + row[i]
                        row[i] = cell.strip('"')

            return render_template('table.html', headers=data[0], rows=data[1:])

        except UnicodeDecodeError as e:
            return jsonify({"error": f"Error: No se pudo decodificar el archivo - {str(e)}"}), 400

        except Exception as e:
            return jsonify({"error": f"Error al procesar el archivo CSV: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"Error inesperado al manejar la solicitud: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
