# CTR_malleability_attack
- Cifra un archivo XML verdadero mediante CTR e identifica los bytes
de ese mensaje cifrado que representan la cabecera conocida

- Extrae el key stream de esa cabecera

- Remplaza con el texto falso de la misma longitud del original y cífralo con el keystream

- Guarda el resultado manipulado y luego descífralo para comprobar que
  el ataque se realizó bien
