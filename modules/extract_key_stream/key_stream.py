from modules.xor.calculatexor.xor import xor
from modules.read_files.read_files import leer_archivo_cabecera
keyStream = "key_stream.key"

"""
//Extracción del key stream de la cabecera original
* Archivo con la cabecera sin cifrar: archivo_cabecera
^ Archivo con la cabecera cifrada: archivo_cabecera_cifrado
"""


def extraer_key_stream_cabecera(archivo_cabecera, archivo_cabecera_cifrado):
    archivo_cabecera_original = leer_archivo_cabecera(archivo_cabecera)
    archivo_cabecera_original_cifrado = leer_archivo_cabecera(archivo_cabecera_cifrado)
    regresar_key_stream = open(keyStream, "wb")
    regresar_key_stream.write(xor(archivo_cabecera_original, archivo_cabecera_original_cifrado))
    regresar_key_stream.close()
    return regresar_key_stream