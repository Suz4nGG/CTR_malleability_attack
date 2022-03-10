from modules.cipher.aesctr.ctr import cifrar, descifrar
from modules.extract_header.extract_header import extraer_cabecera
from modules.extract_key_stream.key_stream import extraer_key_stream_cabecera
from modules.attacker_header_encryption.attacker_header_encryption import cifrar_cabecera_atacante
from modules.spoofing_file.spoofing_file import crear_archivo_final
"""
//Reproduce el ataque anterior con el archivo XML de ejemplo:
* - Cifra un archivo XML verdadero mediante CTR e identifica los bytes de ese mensaje cifrado que representan la cabecera conocida
* - Extrae el key stream de esa cabecera
* - Remplaza con el texto falso de la misma longitud del original y cífralo con el keystream
* - Guarda el resultado manipulado y luego descífralo para comprobar que el ataque se realizó bien
"""

if __name__ == '__main__':
    """
    //Cifrado del archivo XML
    * Algoritmo: CTR
    ^ XML: cliente.xml
    ! Cifrado XML: cliente.xml.ctr
    """
    archivoXMLOriginal = "./cliente/xml/cliente.xml"
    archivoXMLCifrado = "./cliente/xml_ctr/cliente.xml.ctr"
    cifrar(archivoXMLOriginal, archivoXMLCifrado)

    """
    //Extraer la cabecera original del archivo cifrado
    ^ Archivo Cifrado: cliente.xml.ctr
    * Cabecera Conocida: cabecera_conocida.xml.ctr
    ! Archivo Sobrante: contenido_cliente_sin_cabecera.xml.ctr
    """
    cabeceraOriginalCifrado = "./cliente/xml_ctr/cabecera_cliente.xml.ctr"
    xmlClienteSinCabecera = "./cliente/xml_ctr/cliente_sin_cabecera.xml.ctr"

    extraer_cabecera(archivoXMLCifrado, cabeceraOriginalCifrado, xmlClienteSinCabecera)

    """
    //Extraer el keystream de la cabecera original cifrada
    ^ Archivo cabecera original: cliente_cabecera.xml
    ! Archivo cabecera cifrada: cabecera_conocida.xml.ctr
    """
    cabeceraConocida = "./cliente/xml/cliente_cabecera.xml"

    extraer_key_stream_cabecera(cabeceraConocida, cabeceraOriginalCifrado)

    """
    //Remplazo del texto original con el texto del atacante
    ? Ejemplo: "Cabecera original"
    <XML>
      <CredictCardPurchase>
        <Merchant>Telm Aws</Merchant>
    ? Ejemplo: "Cabecera atacante"
    <XML>
      <CredictCardPurchase>
        <Merchant>Evil llc</Merchant>
    ^ Archivo de cabecera atacante: atacante_cabecera.xml
    ! Archivo de cabecera atacante cifrado: atacante_cabecera_cifrada.xml.ctr
    """
    archivoCabeceraAtacante = "./atacante/xml/atacante_cabecera.xml"
    archivoCabeceraAtacanteCifrado = "./atacante/xml_ctr/atacante_cabecera_cifrada.xml.ctr"
    cifrar_cabecera_atacante(archivoCabeceraAtacante, archivoCabeceraAtacanteCifrado)
    crear_archivo_final(archivoCabeceraAtacanteCifrado, xmlClienteSinCabecera, archivoXMLOriginal)

    """
    //Descifrando el archivo creado
    """
    archivoXMLAlterado = "./cliente_alterado.xml"
    descifrar(archivoXMLOriginal, archivoXMLAlterado)
