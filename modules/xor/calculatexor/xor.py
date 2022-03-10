def xor(binario1, binario2):
    bytes1 = list(binario1)
    bytes2 = list(binario2)

    longitud_menor = len(bytes1)
    lista_mas_larga = bytes2
    if len(bytes2) < longitud_menor:
        longitud_menor = len(bytes2)
        lista_mas_larga = bytes1

    res_bytes = []

    for i in range(longitud_menor):
        res_bytes.append(bytes1[i] ^ bytes2[i])
    res_bytes = res_bytes + lista_mas_larga[longitud_menor:]
    return bytes(res_bytes)
