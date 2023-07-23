import jwt

# Token y clave secreta (la misma que se utilizó para firmar el token)
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"
clave_secreta = "Con KeepCoding aprendemos"  # Aquí debes colocar la clave secreta que se usó para firmar el token

try:
    # Validar el token
    payload = jwt.decode(token, clave_secreta, algorithms=["HS256"])
    print("Token válido")
    print("Contenido del token:", payload)
except jwt.ExpiredSignatureError:
    print("El token ha expirado")
except jwt.InvalidTokenError:
    print("Token inválido")