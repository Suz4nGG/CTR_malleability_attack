"""
*
El siguiente código realiza la extracción de la cabecera y del resto del archivo .xml del cliente, previamente cifrado
//Entradas y salidas
^ Archivo original cifrado: path_entrada_cifrada
* Cabecera original extraida: cabecera_original
! Cuerpo del archivo cifrado sin la cabecera: cuerpo_original
"""


def extraer_cabecera(path_entrada_cifrada, cabecera_original, cuerpo_original):
    cabecera_original_archivo = open(cabecera_original, "wb")
    cuerpo_sin_cabecera = open(cuerpo_original, "wb")
    archivo_cifrado_contenido = open(path_entrada_cifrada, "rb").read()
    cabecera_original = archivo_cifrado_contenido[:64]
    cabecera_original_archivo.write(cabecera_original)
    cuerpo_sin_cabecera_salida = archivo_cifrado_contenido[64:]
    cuerpo_sin_cabecera.write(cuerpo_sin_cabecera_salida)
    cabecera_original_archivo.close()
    cuerpo_sin_cabecera.close()
    return cuerpo_sin_cabecera
