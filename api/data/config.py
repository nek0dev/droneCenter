from os import getenv
# from dotenv import load_dotenv
#
# load_dotenv()


JWT_SECRET = getenv("jwt_secret")
JWT_ALGORITHM = getenv("jwt_algorithm")

HASH_SALT = getenv("hash_salt")
