import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoParaCifrar_bytes = bytes('He descubierto el error y no volveré a hacerlo mal', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')

#Tiene que ser aleatoria. Sólo está fijo por enseñanza!!!
nonce = bytes.fromhex('f5871c9ff7f99c926102dd92')

#datos_asociados_bytes = bytes("", "UTF-8")
datos_asociados_bytes = bytes("Esto nos valdrá para validar la integridad y la autenticación pero nunca la confidencialidad.", "UTF-8")


#1) Definimos el cifrador, como hacemos normalmente.
cipher = AES.new(clave, AES.MODE_GCM,nonce=nonce)
#2) Datos asociados. Son datos que no necesitamos cifrar, pero nos importa que nos los cambien
cipher.update(datos_asociados_bytes)

#3) Cifrar y autenticar generando un tag. 
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoParaCifrar_bytes)

#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
nonce_b64 = b64encode(cipher.nonce).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
datos_asociados_b64 = b64encode(datos_asociados_bytes).decode('utf-8')
tag_b64 =b64encode(tag).decode('utf-8')
mensaje_json = json.dumps({'nonce':nonce_b64, 'datos asociados': datos_asociados_b64, 'tag': tag_b64, 'texto cifrado':texto_cifrado_b64})
print(mensaje_json)

