import time

import jwt

from data.config import JWT_SECRET, JWT_ALGORITHM


def decode_jwt(token: str):
    """
    :param token: jwt token
    :return:
    :rtype: None | dict
    """
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except:
        return None
    return decoded_token if decoded_token["expires"] >= time.time() else None
