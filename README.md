# Aplicación Web de Visualización de Datos

Este repositorio contiene una aplicación web desarrollada con Flask para visualizar datos desde archivos CSV.

## Archivos

- **app.py:** Contiene la lógica principal de la aplicación web desarrollada con Flask.
- **index.html:** Página principal de la aplicación que permite la carga de archivos CSV.
- **table.html:** Página para mostrar los datos del archivo CSV en formato de tabla.
- **styles.css:** Archivo de estilos para dar formato a las páginas HTML.
- **table_sort.js:** Script para ordenar dinámicamente los datos en la tabla.

## Detalles de la Aplicación

La aplicación utiliza Flask para proporcionar rutas que permiten cargar archivos CSV y visualizar sus datos en una tabla HTML. A continuación, se detalla la estructura de los archivos principales:

### `app.py`

Este módulo contiene la lógica principal de la aplicación. Incluye rutas para renderizar las páginas HTML y procesar la carga de archivos CSV. Se han incluido comentarios y docstrings para mejorar la comprensión del código.

### `index.html`

Página principal de la aplicación que presenta un formulario para cargar archivos CSV. Se ha añadido un script para permitir la funcionalidad de ordenar dinámicamente los datos en la tabla.

### `table.html`

Página para mostrar los datos del archivo CSV en una tabla HTML. Utiliza estilos definidos en `styles.css`. También incluye el mismo script para ordenar los datos.

### `styles.css`

Archivo de estilos que define la apariencia de la tabla y sus elementos, incluyendo estilos para los encabezados, celdas y filas especiales.

### `table_sort.js`

Script jQuery que permite ordenar dinámicamente los datos de la tabla al hacer clic en los encabezados de las columnas.

## Uso

Para ejecutar la aplicación:

1. Asegúrate de tener Python y Flask instalados.
2. Ejecuta `python app.py` desde la terminal.
3. Accede a `http://localhost:5000/` en tu navegador para cargar un archivo CSV y visualizar los datos.

## Notas Adicionales

- Se han incluido comentarios en el código para mejorar la legibilidad y comprensión.
- Asegúrate de tener los requisitos necesarios antes de ejecutar la aplicación.

¡Disfruta explorando y visualizando tus datos!