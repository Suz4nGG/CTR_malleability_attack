"""
//Lectura de archivos
* Archivo a leer: archivo
"""


def leer_archivo_cabecera(archivo):
    contenido = open(archivo, "rb").read()
    return contenido
