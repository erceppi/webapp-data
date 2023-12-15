from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No se encontró ningún archivo CSV"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Archivo no seleccionado"})

    if file:
        try:
            stream = file.stream.read().decode("UTF8")
            data = [row.split(',') for row in stream.split('\n') if row.strip()]

            if not data:
                return jsonify({"error": "El archivo CSV está vacío"})

            headers = data[0]
            rows = data[1:]

            return render_template('table.html', headers=headers, rows=rows)
        except Exception as e:
            return jsonify({"error": f"Error al procesar el archivo CSV: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
