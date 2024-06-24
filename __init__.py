# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
# Add modules libraries to Rocektbot
# -----------------------------------

import os
import sys

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + "modules" + os.sep + "AWSRedshift" + os.sep + "libs" + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

import redshift_connector
# Globals declared here
global conn
global cursor

module = GetParams("module")

if module == "connect":
    host = GetParams("host")
    port = GetParams("port")
    database = GetParams("db")
    db_user = GetParams("user")
    password = GetParams("pass")
    var_ = GetParams("result")

    try:
        conn = redshift_connector.connect(
            host=host,
            port=port,
            database=database,
            user=db_user,
            password=password
        )

        cursor = conn.cursor()

        SetVar(var_, True)
    except Exception as e:
        SetVar(var_, False)
        PrintException()
        raise Exception(e)

if module == "query":
    query = GetParams("query")
    result = []
    var_ = GetParams("result")

    try:
        cursor.execute(query)

        if query.lower().startswith("select"):

            col = [d[0] for d in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                ob_ = {}
                t = 0
                for r in row:
                    ob_[col[t]] = str(r) + ""
                    t = t + 1
                result.append(ob_)

        elif query.lower().startswith("insert") and "returning" in query.lower():

            col = [d[0] for d in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                ob_ = {}
                t = 0
                for r in row:
                    ob_[col[t]] = str(r) + ""
                    t = t + 1
                result.append(ob_)

            conn.commit()
        else:
            conn.commit()
            result = "True"

        SetVar(var_, result)
    except Exception as e:
        PrintException()
        raise e


if module == "close":
    try:
        cursor.close()
        conn.close()
    except Exception as e:
        PrintException()
        raise e
    