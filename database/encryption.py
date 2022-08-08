import bcrypt


class Encryptor:
    @classmethod
    def encode_password(cls, password: str) -> bytes:
        return password.encode("utf-8")

    @classmethod
    def hash_password(cls, encoded_password):
        return bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    @classmethod
    def is_password_correct(cls, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
