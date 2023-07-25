import time
from typing import Dict

import jwt
from app.settings import settings


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_name: str) -> Dict[str, str]:
    payload = {
        "user_name": user_name,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
