from modules.xor.calculatexor.xor import xor
from modules.read_files.read_files import leer_archivo_cabecera
from modules.extract_key_stream.key_stream import extraer_key_stream_cabecera
keyStream = "key_stream.key"

"""
//Cifrado de la cabecera del atacante bajo el contexto de la key stream de la cabecera original
* archivo_cabecera_atacante: archivo del atacante sin cifrar
^ archivo_cabecera_atacante_cifrado: archivo del atacante ya cifrado
"""

def cifrar_cabecera_atacante(archivo_cabecera_atacante, archivo_cabecera_atacante_cifrado):
    salida_cabecera_atacante = open(archivo_cabecera_atacante_cifrado, 'wb')
    key_stream = leer_archivo_cabecera(keyStream)
    archivo_atacante = leer_archivo_cabecera(archivo_cabecera_atacante)
    salida_cabecera_atacante.write(xor(key_stream, archivo_atacante))
    salida_cabecera_atacante.close()
    return salida_cabecera_atacante
