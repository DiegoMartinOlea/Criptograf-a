from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import binascii
import os

#Se considera "robusto" para la firma. 

my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"


key = RSA.importKey(open(path_file_priv).read())
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')

hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key)
signature = signer.sign(hash)
print("Firma:", signature.hex())
