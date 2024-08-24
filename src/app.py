from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir =os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

    #rutas de la aplicacion
@app.route('/')
def home():
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM soldadores")
        myresult = cursor.fetchall()
        #convertir los datos a diccionario
        insertObject =[]
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        return render_template('index.html', data=insertObject)


    #ruta para guardar soldadores en la bd
@app.route('/user', methods=['POST'])
def addUser():
    RUT = request.form.get('RUT')
    N = request.form.get('N')
    NOMBRE = request.form.get('NOMBRE')
    TURNO = request.form.get('TURNO')
    CARGO = request.form.get('CARGO')
    ALCANCE = request.form.get('ALCANCE')
    ESTAMPA = request.form.get('ESTAMPA')
    FECHA_CALIFICACION = request.form.get('FECHA_CALIFICACION')
    INFORME_LABORATORIO = request.form.get('INFORME_LABORATORIO')
    ESTADO_DE_PAGO_CESMEC = request.form.get('ESTADO_DE_PAGO_CESMEC')
    HABILITADO_PARA_SOLDAR = request.form.get('HABILITADO_PARA_SOLDAR')
    RANGO_DE_DIAMETROS_O_ESPESORES = request.form.get('RANGO_DE_DIAMETROS_O_ESPESORES')
    WPQ_AVA = request.form.get('WPQ_AVA')
    POSICION_CALIFICADA = request.form.get('POSICION_CALIFICADA')
    MATERIAL_BASE = request.form.get('MATERIAL_BASE')
    PROCESO = request.form.get('PROCESO')
    NORMA = request.form.get('NORMA')
    WPS = request.form.get('WPS')
    PQR = request.form.get('PQR')
    ESTATUS = request.form.get('ESTATUS')
    CONTRATADO_FINIQUITADO_O_NO_HABILITADO = request.form.get('CONTRATADO_FINIQUITADO_O_NO_HABILITADO')
    OBSERVACIONES = request.form.get('OBSERVACIONES')
    if RUT and N and NOMBRE and TURNO and ALCANCE and ESTAMPA and FECHA_CALIFICACION and INFORME_LABORATORIO and ESTADO_DE_PAGO_CESMEC and HABILITADO_PARA_SOLDAR and RANGO_DE_DIAMETROS_O_ESPESORES and WPQ_AVA and POSICION_CALIFICADA and MATERIAL_BASE and PROCESO and NORMA and WPS and PQR and ESTATUS and CONTRATADO_FINIQUITADO_O_NO_HABILITADO and OBSERVACIONES:
        cursor = db.database.cursor()
        sql = "INSERT INTO soldadores (RUT, N, NOMBRE, TURNO, CARGO, ALCANCE, ESTAMPA, FECHA_CALIFICACION, INFORME_LABORATORIO, ESTADO_DE_PAGO_CESMEC, HABILITADO_PARA_SOLDAR,RANGO_DE_DIAMETROS_O_ESPESORES, WPQ_AVA,POSICION_CALIFICADA, MATERIAL_BASE, PROCESO,NORMA, WPS, PQR, ESTATUS, CONTRATADO_FINIQUITADO_O_NO_HABILITADO, OBSERVACIONES) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (RUT, N, NOMBRE, TURNO, CARGO, ALCANCE, ESTAMPA, FECHA_CALIFICACION, INFORME_LABORATORIO, ESTADO_DE_PAGO_CESMEC, HABILITADO_PARA_SOLDAR, RANGO_DE_DIAMETROS_O_ESPESORES, WPQ_AVA, POSICION_CALIFICADA, MATERIAL_BASE, PROCESO,NORMA, WPS, PQR, ESTATUS, CONTRATADO_FINIQUITADO_O_NO_HABILITADO, OBSERVACIONES)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

#@app.route('/delete/<string:id>')
#def delete(id):
 #   cursor = db.database.cursor()
  #  sql = "DELETE FROM soldadores WHERE id=%s)"
   # data = (id,)
    #cursor.execute(sql, data)
    #db.database.commit()
    #return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = None  # Inicializa cursor aquí
    try:
        cursor = db.cursor()
        sql = "DELETE FROM soldadores WHERE id=%s"
        data = (id,)
        cursor.execute(sql, data)
        db.commit()
        return redirect(url_for('home'))
    except Exception as e:
        print(f"Error: {e}")
        return "Ocurrió un error al intentar eliminar el trabajador."
    finally:
        if cursor is not None:
            cursor.close()

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    RUT = request.form.get('RUT')
    N = request.form.get('N')
    NOMBRE = request.form.get('NOMBRE')
    TURNO = request.form.get('TURNO')
    CARGO = request.form.get('CARGO')
    ALCANCE = request.form.get('ALCANCE')
    ESTAMPA = request.form.get('ESTAMPA')
    FECHA_CALIFICACION = request.form.get('FECHA_CALIFICACION')
    INFORME_LABORATORIO = request.form.get('INFORME_LABORATORIO')
    ESTADO_DE_PAGO_CESMEC = request.form.get('ESTADO_DE_PAGO_CESMEC')
    HABILITADO_PARA_SOLDAR = request.form.get('HABILITADO_PARA_SOLDAR')
    RANGO_DE_DIAMETROS_O_ESPESORES = request.form.get('RANGO_DE_DIAMETROS_O_ESPESORES')
    WPQ_AVA = request.form.get('WPQ_AVA')
    POSICION_CALIFICADA = request.form.get('POSICION_CALIFICADA')
    MATERIAL_BASE = request.form.get('MATERIAL_BASE')
    PROCESO = request.form.get('PROCESO')
    NORMA = request.form.get('NORMA')
    WPS = request.form.get('WPS')
    PQR = request.form.get('PQR')
    ESTATUS = request.form.get('ESTATUS')
    CONTRATADO_FINIQUITADO_O_NO_HABILITADO = request.form.get('CONTRATADO_FINIQUITADO_O_NO_HABILITADO')
    OBSERVACIONES = request.form.get('OBSERVACIONES')
    if RUT and N and NOMBRE and TURNO and ALCANCE and ESTAMPA and FECHA_CALIFICACION and INFORME_LABORATORIO and ESTADO_DE_PAGO_CESMEC and HABILITADO_PARA_SOLDAR and RANGO_DE_DIAMETROS_O_ESPESORES and WPQ_AVA and POSICION_CALIFICADA and MATERIAL_BASE and PROCESO and NORMA and WPS and PQR and ESTATUS and CONTRATADO_FINIQUITADO_O_NO_HABILITADO and OBSERVACIONES:
        try:
            cursor = db.database.cursor()
            sql = """
                UPDATE soldadores 
                SET RUT = %s, N = %s, NOMBRE = %s, TURNO = %s, CARGO = %s, ALCANCE = %s, 
                    ESTAMPA = %s, FECHA_CALIFICACION = %s, INFORME_LABORATORIO = %s, 
                    ESTADO_DE_PAGO_CESMEC = %s, HABILITADO_PARA_SOLDAR = %s, 
                    RANGO_DE_DIAMETROS_O_ESPESORES = %s, WPQ_AVA = %s, 
                    POSICION_CALIFICADA = %s, MATERIAL_BASE = %s, PROCESO = %s, 
                    NORMA = %s, WPS = %s, PQR = %s, ESTATUS = %s, 
                    CONTRATADO_FINIQUITADO_O_NO_HABILITADO = %s, OBSERVACIONES = %s 
                WHERE id = %s
            """
            data = (RUT, N, NOMBRE, TURNO, CARGO, ALCANCE, ESTAMPA, FECHA_CALIFICACION, 
                    INFORME_LABORATORIO, ESTADO_DE_PAGO_CESMEC, HABILITADO_PARA_SOLDAR, 
                    RANGO_DE_DIAMETROS_O_ESPESORES, WPQ_AVA, POSICION_CALIFICADA, 
                    MATERIAL_BASE, PROCESO, NORMA, WPS, PQR, ESTATUS, 
                    CONTRATADO_FINIQUITADO_O_NO_HABILITADO, OBSERVACIONES, id)
            cursor.execute(sql, data)
            db.database.commit()
            cursor.close()
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return "Error al procesar la solicitud", 500
    else:
        return "Datos incompletos", 400
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)