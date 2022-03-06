from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

#FUNCION QUE REALIZA LA CONECCION A LA BASE DE DATOS
def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host="mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",
            database="bsale_test",
            user="bsale_test",
            password="bsale_test"
        )
    except pymysql.Error as e:
        #Si da error que imprima el error
        print(e)
    return conn

#TABLA PRODUCT CON CATEGORY
@app.route("/productos")
def getProductos():
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute (" SELECT * FROM product INNER JOIN category ON product.category = category.id")
        datos = cursor.fetchall()

        productos=[]

        for x in datos:
            producto = {"id":x[0],"name":x[1],"url_img":x[2],"price":x[3],"discount":x[4],"category_name":x[7]}
            if bool(x[2]):
                productos.append(producto)
        return jsonify({"productos":productos})

    except Exception as ex:
        return jsonify({"mensaje":"error de tabla productos"})

#MOSTRAR DECUENTOS
@app.route("/descuentos")
def getDescuento():
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute (" SELECT * FROM product INNER JOIN category ON product.category = category.id")
        datos = cursor.fetchall()

        productos=[]

        for x in datos:
            producto = {"id":x[0],"name":x[1],"url_img":x[2],"price":x[3],"discount":x[4],"category_name":x[7]}
            
            if not bool(x[2] ):
               pass   
            elif x[4] != 0 and bool(x[2]):
                productos.append(producto)
            else:
                pass
            
        return jsonify({"productos":productos})

    except Exception as ex:
        return jsonify({"mensaje":"error de tabla productos"})

#MOSTRAR POR CATEGORIA
@app.route("/productos/categorias/<orden>")
def getProductoss(orden):

    conn = db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""SELECT product.name,category.name,url_image,price,discount
                FROM product 
                INNER JOIN category ON product.category = category.id
                WHERE category.name = '{0}'""".format(orden))
        datos = cursor.fetchall()

        productos=[]
        for x in datos:
            producto = {"name":x[0],"category_name":x[1],"url_img":x[2],"price":x[3],"discount":x[4]}
            if bool(x[2]):
                productos.append(producto)
        return jsonify({"productos":productos})

    except Exception as ex:
        return jsonify({"mensaje":"error de tabla productos"})

#BUSCADOR POR NOMBRE
@app.route("/productos/<name>")
def getNames(name):

    conn = db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""SELECT product.name,category.name,url_image,price,discount
                FROM product 
                INNER JOIN category ON product.category = category.id
                WHERE product.name LIKE '%{0}%'""".format(name))
        datos = cursor.fetchall()
  
        if (len(datos) > 0):
            productos=[]
            for x in datos:
                producto = {"name":x[0],"category_name":x[1],"url_img":x[2],"price":x[3],"discount":x[4]}
                if bool(x[2]):
                    productos.append(producto)
            return jsonify({"productos":productos})
    
        else:
            return "el producto no existe",404

    except Exception as ex:
        return jsonify({"mensaje":"error de al buscar"})


#MANEJADOR DE ERROR POR PAGINA NO ENCONTRADA
def pagNoEncontrada(error):
    return "<h1>PAGINA NO EXISTE</h1>", 404


#Iniciamos el servidor
if __name__ == "__main__":
    app.run(debug=True)