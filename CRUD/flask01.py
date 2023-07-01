#----------------------------------------------
# Importamos el módulo necesario para gestionar
# la base de datos, y los elementos necesarios
# del framework Flask.
#----------------------------------------------
import sqlite3
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

# Nombre del objeto flask.
app = Flask(__name__)
CORS(app)


# Nombre del archivo que contiene la base de datos.
DATABASE = "paquete.db"


#----------------------------------------------
# Conectamos con la base de datos. 
# Retornamos el conector (conn)
#----------------------------------------------
def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#----------------------------------------------
# Esta funcion crea la tabla "productos" en la
# base de datos, en caso de que no exista.
#----------------------------------------------
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS paquete (
                    id INT PRIMARY KEY,
                    nombre_paquete VARCHAR(100),
                    stock INT,
                    precio FLOAT,
                    region VARCHAR(50),
                    provincias VARCHAR(200))
            """)
    conn.commit()
    cursor.close()
    conn.close()

#----------------------------------------------
# Ruta de inicio
#----------------------------------------------

@app.route('/')
def index():
    return redirect('http://127.0.0.1:5500/CRUD/index.html')


#----------------------------------------------
# Esta funcion da de alta un producto en la
# base de datos.
#----------------------------------------------
@app.route('/paquete', methods=['POST'])
def alta_producto():
    data = request.get_json()
    if 'id' not in data or 'nombre_paquete' not in data or 'stock' not in data or 'precio' not in data or 'region' not in data or 'provincias' not in data:
        return jsonify({'error': 'Falta uno o más campos requeridos'}), 400
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO paquete(id, nombre_paquete, stock, precio, region, provincias)
                    VALUES(?,?,?,?) """,
                    (data['id'], data['nombre_paquete'], data['stock'], data['precio'], data['region'], data['provincias']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'mensaje': 'Alta efectuada correctamente'}), 201
    except:
        return jsonify({'error': 'Error al dar de alta el producto'}), 500
    

#----------------------------------------------
# Muestra en la pantalla los datos de un  
# producto a partir de su código.
#----------------------------------------------
@app.route('/paquete/<int:id>', methods=['GET'])
def consultar_producto(id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM paquete 
                            WHERE id=?""", (id,))
        paquete = cursor.fetchone()
        if paquete is None:
            return jsonify({'error': 'Paquete no encontrado'}), 404
        else:
            return jsonify({
                'id': paquete['id'],
                'nombre_paquete': paquets['nombre_paquete'],
                'stock': paquete['stock'],
                'precio': paquete['precio'],
                'region': paquete['region'],
                'provincias': paquete['provincias']
            })
    except:
        return jsonify({'error': 'Error al consultar el paquete'}), 500


#----------------------------------------------
# Modifica los datos de un producto a partir
# de su código.
#----------------------------------------------
@app.route('/paquete/<int:id>', methods=['PUT'])
def modificar_producto(id):
    data = request.get_json()
    if 'id' not in data or 'nombre_paquete' not in data or 'stock' not in data or 'precio' not in data or 'region' not in data or 'provincias' not in data:
        return jsonify({'error': 'Falta uno o más campos requeridos'}), 400
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM paquete WHERE id=?""", (id,))
        producto = cursor.fetchone()
        if producto is None:
            return jsonify({'error': 'Paquete no encontrado'}), 404
        else:
            cursor.execute("""UPDATE paquete SET nombre_paquete=?, stock=?, precio=?, region=?, provincias=?
                                WHERE id=?""", (data['id'], data['nombre_paquete'], data['stock'], data['precio'], data['region'], data['provincias']))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'mensaje': 'Paquete modificado correctamente'}), 200
    except:
        return jsonify({'error': 'Error al modificar el producto'}), 500


#----------------------------------------------
# Lista todos los productos en la base de datos.
#----------------------------------------------
@app.route('/paquete', methods=['GET'])
def listar_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM paquete")
        productos = cursor.fetchall()
        response = []
        for paquete in productos:
            response.append({
                'id': paquete['id'],
                'nombre_paquete': paquete['nombre_paquete'],
                'stock': paquete['stock'],
                'precio': paquete['precio'],
                'region': paquete['region'],
                'provincias': paquete['provincias']
            })
        return jsonify(response)
    except:
        return jsonify({'error': 'Error al listar los productos'}), 500



#----------------------------------------------
# Ejecutamos la app
#----------------------------------------------
if __name__ == '__main__':
    crear_tabla()
    app.run()

