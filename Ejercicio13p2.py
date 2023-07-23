import ed25519


publickey = open("ed25519-publ","rb").read()
privatekey = open("ed25519-priv","rb").read()

signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')
#signature = b'78613ae771b5b220d2a72008d7cf3bc6f232547692b02d38ffc671c70eb2015dc697252fbefa087995b2379e1422044cd1dcd03b631351188e1ae62a5dc27701'
print("Firma Generada (64 bytes):", signature)

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")