
# Primeiro instalar o jwt
# pip install pyjwt

import jwt

import datetime
from time import sleep

# Definir uma chave secreta
secrete_key = "xijfkdsjfkdsjfkldsjgkdjsgksd"

# No payload colocamos dados como a expiração do token ou alguns dados dos usuarios
payload = {
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=2),
    'user': 1
}


def createToke() -> str:
    
    token = jwt.encode(
        payload= payload,
        key= secrete_key,
        algorithm="HS256"
    )
    
    return token

def descriptography(t) -> str:
    sleep(5)
    return jwt.decode(t, algorithms="HS256", key=secrete_key)


token = createToke()

print(token)

print(descriptography(token))

