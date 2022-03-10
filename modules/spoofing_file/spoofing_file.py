"""
//Unir el archivo de la cabecera del atacante con el cuerpo del original del archivo del cliente
* Archivo de la cabecera del atacante previamente cifrada con el key stream original: cabecera_atacante_cifrado
^ Archivo del cuerpo original del cliente: cuerpo_sin_cabecera
! Archivo de salida cifado: archivo_XML_cifrado
"""


def crear_archivo_final(cabecera_atacante_cifrado, cuerpo_sin_cabecera, archivo_XML_cifrado):
    archivo_final_xml = open(archivo_XML_cifrado, "wb")
    cabecera = open(cabecera_atacante_cifrado, "rb").read()
    cliente_mitad = open(cuerpo_sin_cabecera, "rb").read()
    archivo_final_xml.write(cabecera)
    archivo_final_xml.write(cliente_mitad)
    archivo_final_xml.close()
    return archivo_final_xml
