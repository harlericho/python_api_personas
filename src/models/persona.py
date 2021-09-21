from config.db import cadenaConexion
import config.validation
validar = config.validation
def listadoPersona():
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos"
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def listadoPersonaID(id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE id = ?"
        cur.execute(sql,[id])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def guardarPersona(dni,nombres,fecha,correo):
    if validar.validarDni(dni):
        return ["dni","Dni es requerido"]
    elif validar.validarMaximoDni(dni):
        return ["dni","Dni debe ser 10 caracteres"]
    elif validar.validarDniNumerico(dni) != True:
        return ["dni","Dni debe ser numerico"]
    elif validar.validarNombres(nombres):
        return ["nombres","Nombres es requerido"]
    elif validar.validarFecha(fecha):
        return ["fecha","Fecha es requerido"]
    elif validar.validarCorreo(correo):
        return ["correo","Correo es requerido"]
    elif validar.validarCorreoReal(correo):
        return ["correo","Correo no tiene el formato idoneo"]
    else:
        try:
            db = cadenaConexion()
            cur = db.cursor()
            sql ="INSERT INTO datos (dni,nombres,fecha,correo) VALUES (?,?,?,?)"
            cur.execute(sql,[dni,nombres,fecha,correo])
            db.commit()
            return "Persona guardado"
        except Exception as e:
            return e
        finally:
            cur.close()
            db.close()

def actualizarPersona(dni,nombres,fecha,correo,id):
    if validar.validarDni(dni):
        return ["dni","Dni es requerido"]
    elif validar.validarMaximoDni(dni):
        return ["dni","Dni debe ser 10 caracteres"]
    elif validar.validarDniNumerico(dni) != True:
        return ["dni","Dni debe ser numerico"]
    elif validar.validarNombres(nombres):
        return ["nombres","Nombres es requerido"]
    elif validar.validarFecha(fecha):
        return ["fecha","Fecha es requerido"]
    elif validar.validarCorreo(correo):
        return ["correo","Correo es requerido"]
    elif validar.validarCorreoReal(correo):
        return ["correo","Correo no tiene el formato idoneo"]
    else:
        try:
            db = cadenaConexion()
            cur = db.cursor()
            sql ="UPDATE datos SET dni= ?, nombres = ?, fecha = ?, correo = ? WHERE id = ?"
            cur.execute(sql,[dni,nombres,fecha,correo,id])
            db.commit()
            return "Persona actualizada"
        except Exception as e:
            return e
        finally:
            cur.close()
            db.close()

def eliminarPersona(id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="DELETE FROM datos WHERE id = ?"
        cur.execute(sql,[id])
        db.commit()
        return "Persona eliminada"
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarDni1(dni):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE dni = ?"
        cur.execute(sql,[dni])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def validarDni2(dni,id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT COUNT(*) FROM datos WHERE dni=? OR id=?"
        cur.execute(sql,[dni,id])
        return cur.fetchone()[0]
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarCorreo1(correo):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE correo = ?"
        cur.execute(sql,[correo])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarCorreo2(correo,id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT COUNT(*) FROM datos WHERE correo=? OR id=?"
        cur.execute(sql,[correo,id])
        return cur.fetchone()[0]
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()