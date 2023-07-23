import hashlib

texto = "En KeepCoding aprendemos cómo protegernos con criptografía"
hash_obj = hashlib.sha3_256(texto.encode('utf-8'))
sha3_256_hash = hash_obj.hexdigest()

print("Texto original:", texto)
print("SHA3-256 Hash:", sha3_256_hash)