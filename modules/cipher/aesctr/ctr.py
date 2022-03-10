import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

iv = base64.b64decode('AQXY/aOvVyr6g0ma3e33/g=='.encode('utf-8'))
key = base64.b64decode('vsl7nzcAc7ibYSvybs9vMw=='.encode('utf-8'))


def cifrar(path_entrada, path_salida):
    salida_archivo = open(path_salida, 'wb')
    aesCipher = Cipher(algorithms.AES(key),
                       modes.CTR(iv),
                       backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    for buffer in open(path_entrada, 'rb'):
        salida_archivo.write(aesEncryptor.update(buffer))
    aesEncryptor.finalize()
    salida_archivo.close()


def descifrar(path_entrada, path_salida):
    salida_archivo = open(path_salida, 'wb')
    aesCipher = Cipher(algorithms.AES(key),
                       modes.CTR(iv),
                       backend=default_backend())
    aesDecryptor = aesCipher.decryptor()
    for buffer in open(path_entrada, 'rb'):
        print(buffer)
        salida_archivo.write(aesDecryptor.update(buffer))
    aesDecryptor.finalize()
    salida_archivo.close()


if __name__ == '__main__':
    operacion = sys.argv[1]
    path_entrada = sys.argv[2]
    path_salida = sys.argv[3]
    if operacion == 'cifrar':
        cifrar(path_entrada, path_salida)
    elif operacion == 'descifrar':
        descifrar(path_entrada, path_salida)
    else:
        exit(1)
